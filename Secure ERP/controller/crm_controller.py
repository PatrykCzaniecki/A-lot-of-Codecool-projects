from model.crm import crm
from view import terminal as view
from model import data_manager, util

DATAFILE = "C:/Users/Patryk/Codecool/secure-erp-python-mateuszski/model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
table = data_manager.read_table_from_file(DATAFILE)

def list_customers():
    view.print_general_results(crm.list_customers(), "This is a list of our customers!")     


def add_customer():
    view.print_table(crm.add_customer(table), HEADERS) 


def update_customer():
    view.print_table(crm.update_customer(table), HEADERS) 


def delete_customer():
    view.print_table(crm.delete_customer(table), HEADERS) 


def get_subscribed_emails():
    view.print_general_results(crm.get_subscribed_emails(table), "This is a list of emails that subscribe to us!") 


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)