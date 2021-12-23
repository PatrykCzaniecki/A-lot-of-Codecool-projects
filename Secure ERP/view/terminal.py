from tabulate import tabulate


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f'\n{title}:')
    for i in range(1, len(list_options)):
        print(f'({i}) {list_options[i]}')
    print(f'({0}) {list_options[0]}')


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if isinstance(result, int):
        print(f'{label}: {result}')
    elif isinstance(result, float):
        print(label,':', "{:.2f}".format(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        print(f'{label}: ')
        for i in result:
            print(i, end='')
    elif isinstance(result, dict):
        print(label)
        for i, j in result.items():
            print(f'{i}: {j};', end=' ')


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, head):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print(tabulate(table, headers=head, tablefmt="fancy_grid"))


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f'{label}: ')
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    list_of_user_inputs = []
    for i in labels:
        user_input = input(f'{i}:')
        list_of_user_inputs.append(user_input)
    return list_of_user_inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f'Error: {message}!')