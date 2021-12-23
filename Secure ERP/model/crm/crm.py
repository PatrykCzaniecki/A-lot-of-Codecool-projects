""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model\crm\crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def list_customers():
    name_index = 1
    list_of_customers = []
    table = data_manager.read_table_from_file(DATAFILE)
    for i in table:
        list_of_customers.append(i[name_index])
    new_list = ["\n".join(list_of_customers)]
    return new_list


def add_customer(table): 
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    name = input("Enter new customer's username: ")
    email = input(f"For {name} enter email address: ")
    sub = input(f"Is {name} subscribed to the newsletter? (1: yes, 0: no): ")
    record = [id, name, email, sub]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    print(f"New customer {name} has been added! His id number is {id}. His email address is {email}. His sub-value is {sub}") 
    return table


def update_customer(table):
    id_index = 0
    name_index = 1
    email_index = 2
    sub_index = 3
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    customer_to_update = input("Please provide id number of customer you want to update: ")
    for line in table:
        if line[id_index] == customer_to_update:
            print(f"You choose {line[name_index]} to update!")
            update = input(f"Please provide category to update for {line[name_index]} (id, name, email, sub): ")
            if update == "id".lower():
                line[id_index] = id
                print(f"Id for {line[name_index]} has been changed!")
            elif update == "name".lower():
                old_name = line[name_index]
                new_name = input(f"Please provide new name for {old_name}: ")
                line[name_index] = new_name 
                print(f"Name for {old_name} has been changed! Now {old_name}'s name is {new_name}.")
            elif update == "email".lower():
                line[email_index] = input(f"Please provide new email for {line[name_index]}: ")
                print(f"Email adress for {line[name_index]} has been changed!")
            elif update == "sub".lower():
                line[sub_index] = input(f"Please provide new sub-value for {line[name_index]}: ")
                print(f"Subscription value for {line[name_index]} has been changed!")
            else:
                print(f"There isn't id number {customer_to_update} in file! Please choose correct customer.")
                return update_customer(table) 
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table

        
def delete_customer(table):
    id_index = 0
    table = data_manager.read_table_from_file(DATAFILE)
    customer_to_delete = input("Please provide id number of customer you want to remove: ")
    for line in table:
        if line[id_index] == customer_to_delete:
            table.remove(line)
            print(f"Customer with id number {customer_to_delete} has been removed!") 
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table


def get_subscribed_emails(table):
    email_index = 2
    sub_index = 3
    list_subscribed_emails = []
    table = data_manager.read_table_from_file(DATAFILE)
    for line in table:
        if line[sub_index] == "1":
            sub_email = str(line[email_index])
            list_subscribed_emails.append(sub_email)
    new_list = ["\n".join(list_subscribed_emails)]
    return new_list