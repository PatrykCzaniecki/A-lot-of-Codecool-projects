""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import re
from model import data_manager, util
import pandas as pd 


DATAFILE = "model\sales\sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def list_transactions():
    return data_manager.read_table_from_file(DATAFILE)


def add_transaction():
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    customer = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    product = input("Name of product: ")
    price = input("Price of product: ")
    year = input("Year of transaction: ")
    month = input("Month of transaction: ")
    day = input("Day of transaction: ")
    date = f'{year}-{month}-{day}'
    record = [id, customer, product, price, date]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    print("New transaction has been added!") 
    return table


def update_transaction():
    id_index = 0
    customer_index = 1
    product_index = 2
    price_index = 3
    date_index = 4
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    transaction_to_update = input("Please provide id number of transaction you want to update:")
    for line in table:
        if line[id_index] == transaction_to_update:
            print(f"You choose {line[customer_index]} to update!")
            update = input(f"Please provide category to update for {id_index} (id, customer, product, price, date): ")
            if update == "id".lower():
                line[id_index] = id
                print(f"Id for {line[id_index]} has been changed!")
            elif update == "customer".lower():
                old_name = line[customer_index]
                line[customer_index] = id
                print(f"Customer for {old_name} has been changed! Now {old_name}'s name is {id}.")
            elif update == "product".lower():
                line[product_index] = input(f"Please provide new product name for {line[product_index]}: ")
                print(f"Product name for {line[id_index]} has been changed!")
            elif update == "price".lower():
                line[price_index] = input(f"Please provide new price for {line[id_index]}: ")
                print(f"Price for {line[id_index]} has been changed!")
            elif update == "date".lower():
                year = input("Enter year: ")
                month = input("Enter month: ")
                day = input("Enter day: ")
                line[date_index] = f'{year}-{month}-{day}'
                print(f"Date for {line[id_index]} has been changed ")
            else:
                print(f"There isn't id like {transaction_to_update} in file! Please choose correct customer.")
                return update_transaction() 
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table


def delete_transaction():
    id_index = 0
    table = data_manager.read_table_from_file(DATAFILE)
    customer_to_delete = input("Please provide id number of transaction you want to remove: ")
    for line in table:
        if line[id_index] == customer_to_delete:
            table.remove(line)
            print(f"Transaction with id number {customer_to_delete} has been removed!")
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table


def get_biggest_revenue_transaction():
    transaction_list = data_manager.read_table_from_file(DATAFILE)
    transaction_id = ['not_given']
    id_index = 0
    value_index = 3
    max_value = 0
    for line in transaction_list:
        if float(line[value_index]) > max_value:
            transaction_id[id_index] = line[id_index]
            max_value = float(line[value_index])
    return transaction_id[id_index]


def get_biggest_revenue_product():
    product_index = 2
    price_index = 3
    dict_of_products = {}
    list_of_products = []
    table = data_manager.read_table_from_file(DATAFILE)
    for line in table:
        if line[product_index] in line:
            list_of_products.append(line[product_index])
            dict_of_products[f"{line[product_index]}"] = line[price_index]
    number_of_products_in_list = dict([(i, list_of_products.count(i)) for i in list_of_products])
    prices_of_products = list(dict_of_products.values())
    amound_of_products = list(number_of_products_in_list.values())
    count_dict = []
    for i in range(len(number_of_products_in_list)):
        count_dict.append(float(prices_of_products[i]) * float(amound_of_products[i]))
    auxiliary_list = []
    for i in list_of_products:
        if i in auxiliary_list:
            pass
        else:
            auxiliary_list.append(i) 
    new_dict = {}
    for i in range(len(auxiliary_list)):
        new_dict[auxiliary_list[i]] = count_dict[i] 
    max_value_product = max(new_dict, key = new_dict.get) 
    return max_value_product
    

def count_transactions_between():
    id = []
    customer = []
    product = []
    price = []
    date = []
    file = data_manager.read_table_from_file(DATAFILE)
    for line in file:
        id.append(line[0])
        customer.append(line[1])
        product.append(line[2])
        price.append(line[3])
        date.append(line[4])
    new_dict = {}
    new_dict[HEADERS[0]] = id
    new_dict[HEADERS[1]] = customer
    new_dict[HEADERS[2]] = product
    new_dict[HEADERS[3]] = price
    new_dict[HEADERS[4]] = date
    year1 = input("Enter starting year: ")
    month1 = input("Enter starting month: ")
    day1 = input("Enter starting day: ")
    year2 = input("Enter ending year: ")
    month2 = input("Enter ending month: ")
    day2 = input("Enter ending day: ")
    data_from_file = pd.DataFrame(new_dict)
    start_date = f'{year1}-{month1}-{day1}'
    end_date = f'{year2}-{month2}-{day2}'
    mask = (data_from_file['Date'] > start_date) & (data_from_file['Date'] <= end_date)
    data_from_file = data_from_file.loc[mask]
    return len(data_from_file)


def sum_transactions_between():
    id = []
    customer = []
    product = []
    price = []
    date = []
    file = data_manager.read_table_from_file(DATAFILE)
    for line in file:
        id.append(line[0])
        customer.append(line[1])
        product.append(line[2])
        price.append(line[3])
        date.append(line[4])
    new_dict = {}
    new_dict[HEADERS[0]] = id
    new_dict[HEADERS[1]] = customer
    new_dict[HEADERS[2]] = product
    new_dict[HEADERS[3]] = price
    new_dict[HEADERS[4]] = date
    year1 = input("Enter starting year: ")
    month1 = input("Enter starting month: ")
    day1 = input("Enter starting day: ")
    year2 = input("Enter ending year: ")
    month2 = input("Enter ending month: ")
    day2 = input("Enter ending day: ")
    data_from_file = pd.DataFrame(new_dict)
    start_date = f'{year1}-{month1}-{day1}'
    end_date = f'{year2}-{month2}-{day2}'
    mask = (data_from_file['Date'] > start_date) & (data_from_file['Date'] <= end_date)
    data_from_file = data_from_file.loc[mask]
    data_from_file['Price'] = data_from_file['Price'].astype(float)
    total = data_from_file['Price'].sum()
    return total 