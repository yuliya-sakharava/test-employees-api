import pytest
import requests
from env_setup import Credentials, Endpoints
from support.custom_errors import TokenNotFoundError, TokenNotGeneratedError
from endpoints.employees import Employees
from database.db_connection import DatabaseConnection
import json
import time
from env_setup import PATH_SINGLE_EMPLOYEE, PATH_ALL_EMPLOYEES, PATH_DATASET
from support.logger import log_func
from support.json_handler import JSONHandler

# ************************ DB fixtures ************************

LOG = log_func()


@pytest.fixture(scope="session", autouse=True)
def db_connection():
    connection = DatabaseConnection(
        dbname="postgres",
        user="postgres",
        password="Zara2022",
        host="localhost",
        port="5432"
    )
    LOG.info(f"Connection to DB using creds: {connection.connection}")
    yield connection

    connection.close()


@pytest.fixture(scope="session", autouse=True)
def create_employees(db_connection):
    created_users = []
    cur = db_connection.connection.cursor()
    cur.execute("SELECT MAX(employee_id) FROM employees")
    max_employee_id = cur.fetchone()[0]
    cur.close()

    user_data_list = [
        {"name": "Eddy", "organization": "IT", "role": "Lead Developer"},
        {"name": "Jack", "organization": "Finance", "role": "Accountant"},
        {"name": "Ariel", "organization": "Marketing", "role": "Marketing Specialist"}
    ]

    for user_data in user_data_list:
        max_employee_id = max_employee_id + 1 if max_employee_id is not None and max_employee_id != 0 else 1
        user_id = db_connection.fetchone(
            "INSERT INTO employees (employee_id, name, organization, role) VALUES (%s, %s, %s, %s) RETURNING employee_id",
            max_employee_id, user_data["name"], user_data["organization"], user_data["role"]
        )[0]

        user_info = {
            "employeeId": user_id,
            "name": user_data["name"],
            "organization": user_data["organization"],
            "role": user_data["role"]
        }
        created_users.append(user_info)

        db_connection.connection.commit()

    if created_users:
        JSONHandler.dump_json(PATH_DATASET, created_users)

    LOG.info(f"Test dataset has been created: {created_users}")

    return created_users


@pytest.fixture(scope="session", autouse=True)
def read_dataset(create_employees):
    data = JSONHandler.load_json(PATH_DATASET)
    return data


@pytest.fixture(scope="session", autouse=True)
def delete_employees(db_connection, create_employees):
    yield
    time.sleep(10)
    for user in create_employees:
        user_id = user.get("employeeId")
        db_connection.execute("DELETE FROM employees WHERE employee_id = %s", user_id)
    LOG.info("******* Test data has been removed. ")


# ************************ App fixtures ************************

@pytest.fixture(scope="session")
def create_session():
    yield requests.Session()


@pytest.fixture(scope="session")
def credentials():
    return Credentials.get_env_variables()


@pytest.fixture(scope="session")
def bearer_token(credentials):
    response = requests.post(f"{Endpoints.TOKEN_URL}",
                             json={"username": credentials.APP_USERNAME, "password": credentials.APP_PASSWORD},
                             headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        token = response.json().get("token")
        if token is None:
            raise TokenNotFoundError
        yield token
    else:
        raise TokenNotGeneratedError(response.status_code)


@pytest.fixture()
def employees_instance(create_session, bearer_token):
    yield Employees(create_session, Endpoints.EMPLOYEES_URL, bearer_token)
