from model.hr import hr
from view import terminal as view
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def list_employees():
    view.print_table(hr.list_employees(), hr.HEADERS)


def add_employee():
    view.print_table(hr.add_employee(), hr.HEADERS)


def update_employee():
    view.print_table(hr.update_employee(), hr.HEADERS)


def delete_employee():
    view.print_table(hr.delete_employee(), hr.HEADERS)


def get_oldest_and_youngest():
    view.print_general_results(hr.get_oldest_and_youngest, "min/max")


def get_average_age():
    view.print_general_results(hr.get_average_age(), 'Average age of employees')


def next_birthdays():
    view.print_general_results(hr.next_birthdays(), 'Employees that have birthdays within two weeks from input date')


def count_employees_with_clearance():
    view.print_general_results(hr.count_employees_with_clearance(), 'Number of employees with clearance')


def count_employees_per_department():
    view.print_general_results(hr.count_employees_per_department(), 'Number of employees per department')


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)