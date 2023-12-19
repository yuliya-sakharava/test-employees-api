import pytest
import allure
from env_setup import PATH_DATASET
from support.json_handler import JSONHandler


@allure.description('Fetch single employee. Positive case - Fetch single existing employee')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (positive case)')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("employee_id, expected_data",
                         [(data['employeeId'], data) for data in JSONHandler.load_json(PATH_DATASET)],
                         ids=['employee_1', 'employee_2', 'employee_3'])
def test_fetch_single_employee_positive_case(employees_instance, employee_id, expected_data):
    employees_instance.fetch_single_employee_positive_case(employee_id=employee_id, data=expected_data)


# Same as the above function, but without parameterization
# def test_fetch_single_employee_positive_case(employees_instance, read_dataset):
#     employees_instance.fetch_single_employee_positive_case(employee_id=str(read_dataset[0]["employeeId"]),
#                                                            data=read_dataset[0])


@allure.description('Fetch single employee. Negative case - Fetch single non-existing employee')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (negative case)')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_fetch_single_employee_negative_case(employees_instance, read_dataset):
    employees_instance.fetch_single_employee_negative_case(
        employee_id=str(len(read_dataset) + 2))


@allure.description('Fetch all employees')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch all employees')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_fetch_all_employees(employees_instance, read_dataset):
    employees_instance.fetch_all_employees(
        data=read_dataset)


@allure.description('Create new employee')
@allure.label('owner', 'Yuliya')
@allure.title('Create new employee')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_new_employee(employees_instance, read_dataset):
    employees_instance.create_new_employee(
        employee_id=str(len(read_dataset) + 1))


@allure.description('Update a specific field for one employee')
@allure.label('owner', 'Yuliya')
@allure.title('Update single field')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_update_single_field(employees_instance):
    employees_instance.update_single_field(
        employee_id=JSONHandler.load_json(PATH_DATASET)[0]['employeeId'],
        new_data='Marketing')


@allure.description('Update full data for particular employee')
@allure.label('owner', 'Yuliya')
@allure.title('Update all fields')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_full_employee(employees_instance):
    employees_instance.update_full_employee(
        employee_id=JSONHandler.load_json(PATH_DATASET)[2]['employeeId'],
        new_data={"name": "Jacob", "organization": "IT", "role": "Senior Developer"})


@allure.description('Delete single employee')
@allure.label('owner', 'Yuliya')
@allure.title('Delete single employee')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(employees_instance, read_dataset):
    employees_instance.delete_employee(
        employee_id=str(len(read_dataset) + 1))
