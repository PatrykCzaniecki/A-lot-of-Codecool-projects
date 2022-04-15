import os
import psycopg2
import psycopg2.extras


def establish_connection(connection_data=None):
    """
    Create a database connection based on the :connection_data: parameter

    :connection_data: Connection string attributes

    :returns: psycopg2.connection
    """
    if connection_data is None:
        connection_data = get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
                                                                     connection_data['user'],
                                                                     connection_data['host'],
                                                                     connection_data['password'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_unset_vars(var_names):
    return [name for name in var_names if os.environ.get(name) is None]


def unset_var_error_msg(env_vars):
    return f'You should set environmental variables: {", ".join(env_vars)}'


def ensure_var(name):
    value = os.environ.get(name)

    if not value:
        raise ValueError(f'Environmental variable should be set: {name}')
    return value


def get_connection_data(db_name=None):
    """
    Give back a properly formatted dictionary based on the environment variables values which are started
    with :MY__PSQL_: prefix

    :db_name: optional parameter. By default it uses the environment variable value.
    """
    if db_name is None:
        db_name = ensure_var('MY_PSQL_DBNAME')

    return {
        'dbname': db_name,
        'host': ensure_var('MY_PSQL_HOST'),
        'password': ensure_var('MY_PSQL_PASSWORD'),
        'user': ensure_var('MY_PSQL_USER')
    }


def execute_script_file(file_path):
    """
    Execute script file based on the given file path.
    Print the result of the execution to console.

    Example:
    > execute_script_file('db_schema/01_create_schema.sql')

    :file_path: Relative path of the file to be executed.
    """
    package_directory = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(package_directory, file_path)
    with open(full_path) as script_file:
        with establish_connection() as conn, \
                conn.cursor() as cursor:
            try:
                sql_to_run = script_file.read()
                cursor.execute(sql_to_run)
                print("{} script executed successfully.".format(file_path))
            except Exception as ex:
                print("Execution of {} failed".format(file_path))
                print(ex.args)


def execute_select(statement, variables=None, fetchall=True):
    """
    Execute SELECT statement optionally parameterized.
    Use fetchall=False to get back one value (fetchone)

    Example:
    > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})

    statement: SELECT statement

    variables:  optional parameter dict, optional parameter fetchall"""
    result_set = []
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set


def execute_dml_statement(statement, variables=None):
    """
    Execute data manipulation query statement (optionally parameterized)

    :statment: SQL statement

    :variables:  optional parameter dict"""
    result = None
    with establish_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(statement, variables)
            try:
                result = cursor.fetchone()
            except psycopg2.ProgrammingError as pe:
                pass
    return result
