""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import date, timedelta
from model import data_manager, util


DATAFILE = 'C:/1Code/Projects/secure-erp-python-mateuszski/model/hr/hr.csv'
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
table = data_manager.write_table_to_file


def list_employees():
    return data_manager.read_table_from_file(DATAFILE)


def add_employee():
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id()
    name = input("Enter new employee's name: ")
    date_of_bith = input(f"{name} type date of birth: ")
    department = input(f"{name} which department are you working for?: ")
    clearance = input(f"{name} yours clearance is?: ")
    record = [id, name, date_of_bith, department, clearance]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    print(f"New employee {name} has been added! His id number is {id}. His date of birth is {date_of_bith}. His department is {department}")
    return table


def update_employee():
    id_index = 0
    name_index = 1
    birthday_index = 2
    department_index = 3
    clearance_index = 4
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                          number_of_capital_letters=2,
                          number_of_digits=2,
                          number_of_special_chars=2,
                          allowed_special_chars=r"_+-!")
    employee_to_update = input(
        "Please provide id number of customer you want to update: ")
    for line in table:
        if line[id_index] == employee_to_update:
            print(f"You choose {line[name_index]} to update!")
            new_id = input(
                f"Please write 'yes' for id to update for {line[name_index]}. It will automatically change. If not, press enter: ")
            new_name = input(
                f"Please provide name to update for {line[name_index]}. If not, press enter: ")
            new_birthday = input(
                f"Please provide birthday(yyyy-mm-dd) to update for {line[name_index]}. If not, press enter: ")
            new_department = input(
                f"Please provide department to update for {line[name_index]}. If not, press enter: ")
            new_clearance = input(
                f"Please provide clerane lvl to update for {line[name_index]}. If not, press enter: ")
            if new_id == 'yes':
                line[id_index] = id
            if new_name != '':
                line[name_index] = new_name
            if new_birthday != '':
                line[birthday_index] = new_birthday
            if new_department != '':
                line[department_index] = new_department
            if new_clearance != '':
                line[clearance_index] = new_clearance
            data_manager.write_table_to_file(DATAFILE, table, separator=';')
            return table
    print(
        f"There isn't name like {employee_to_update} in file! Please choose correct customer.")
    return table


def delete_employee():
    id_index = 0
    table = data_manager.read_table_from_file(DATAFILE)
    employee_to_delete = input(
        "Please provide id number of employee you want to remove: ")
    for line in table:
        if line[id_index] == employee_to_delete:
            table.remove(line)
            print(
                f"Employee with id number {employee_to_delete} has been removed!")
            data_manager.write_table_to_file(DATAFILE, table, separator=';')
            return table
    print(
        f"There isn't id number like {employee_to_delete} in file! Please choose correct employee.")


def get_oldest_and_youngest():
    table = data_manager.read_table_from_file(DATAFILE)
    name_index = 1
    year_index = 2
    youngest_person_touple = ()
    oldest_person_touple = ()
    for line in table:
        name_and_year_dict = {line[name_index]: line[year_index]}
    for key, value in name_and_year_dict.items():
        if value == min(name_and_year_dict.values()):
            youngest_person_touple = (key)
        elif value == max(name_and_year_dict.values()):
            oldest_person_touple = (key)
    return youngest_person_touple, oldest_person_touple


def get_average_age():
    birthday_index = 2
    files = data_manager.read_table_from_file(DATAFILE)
    list_of_birthdays = []
    for i in files:
        list_of_birthdays.append(i[birthday_index])
    list_of_ages = []
    for j in list_of_birthdays:
        j = j.split('-')
        today = date.today()
        list_of_ages.append(
            today.year - int(j[0]) - ((today.month, today.day) < (int(j[1]), int(j[2]))))
    average_age = sum(list_of_ages)/(len(list_of_ages))
    return average_age


def next_birthdays():
    input_date = input('Write a date year/month/day: ').split('/')
    start_date = date(int(input_date[0]), int(
        input_date[1]), int(input_date[2]))
    days = timedelta(14)
    two_weeks_ahead_data = start_date + days
    delta = two_weeks_ahead_data - start_date
    list_of_days = []
    employees_names = []
    birthday_index = 2
    name_index = 1
    for i in range(delta.days+1):
        day = start_date + timedelta(days=i)
        list_of_days.append(day)
    list_of_files = data_manager.read_table_from_file(DATAFILE)
    for i in list_of_files:
        birthday_date = i[birthday_index].split('-')
        birthday = date(int(input_date[0]), int(
            birthday_date[1]), int(birthday_date[2]))
        if birthday in list_of_days:
            employees_names.append(i[name_index])
    return employees_names


def count_employees_with_clearance():
    clearance_index = 4
    list = data_manager.read_table_from_file(DATAFILE)
    count_employees = 0
    for i in list:
        if i[clearance_index] != '':
            count_employees += 1
    return count_employees


def count_employees_per_department():
    list_of_departments = []
    deparments_index = 3
    list = data_manager.read_table_from_file(DATAFILE)
    dictionary_of_deparments = {}
    for i in list:
        if i[deparments_index] in list_of_departments:
            pass
        else:
            list_of_departments.append(i[deparments_index])
    for i in list_of_departments:
        count = 0
        for j in list:
            if i in j:
                count += 1
        dictionary_of_deparments[i] = count
    return dictionary_of_deparments