import pytest
import allure


# existing_employee = [1, {"employeeId": 1, "name": "Eddy", "organization": "IT", "role": "Lead Developer"}]
# non_existing_employee = [303, {"error": "Employee not found"}]
#
#
# @pytest.mark.parametrize("employee_id, expected_data",
#                          (existing_employee, non_existing_employee),
#                          ids=['existing_employee', 'non_existing_employee'])
# def test_fetch_single_employee(employees_instance, employee_id, expected_data):
#     employees_instance.fetch_single_employee(employee_id=employee_id, data=expected_data)

@allure.description('Fetch single employee. Positive case - Fetch single existing employee.')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (positive case).')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_fetch_single_employee_positive_case(employees_instance, read_dataset):
    employees_instance.fetch_single_employee_positive_case(employee_id=str(read_dataset[0]["employeeId"]),
                                                           data=read_dataset[0])


@allure.description('Fetch single employee. Negative case - Fetch single non-existing employee.')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch single employee (negative case).')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_fetch_single_employee_negative_case(employees_instance, read_dataset):
    employees_instance.fetch_single_employee_negative_case(employee_id=str(len(read_dataset) + 1))


@allure.description('Fetch all employees.')
@allure.label('owner', 'Yuliya')
@allure.title('Fetch all employees.')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_fetch_all_employees(employees_instance, read_dataset):
    employees_instance.fetch_all_employees(data=read_dataset)


@allure.description('Delete single employee.')
@allure.label('owner', 'Yuliya')
@allure.title('Delete single employee.')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_employee(employees_instance, read_dataset):
    employees_instance.delete_employee(employee_id=str(read_dataset[0]["employeeId"]))

    # def test_create_new_employee(employees_instance):
    #     employees_instance.create_new_employee()
    #
    #
    # def test_update_single_field(employees_instance):
    #     employees_instance.update_single_field()
    #
    #
    # def test_update_full_employee(employees_instance):
    #     employees_instance.update_full_employee()
