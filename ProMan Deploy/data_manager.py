import os
import psycopg2
import psycopg2.extras
import queries
import bcrypt

connection_string = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(connection_string)


def establish_connection():
    """
    Create a database connection based on the :connection_data: parameter
    :connection_data: Connection string attributes
    :returns: psycopg2.connection
    """
    try:
        connection_string = os.environ.get("DATABASE_URL")
        conn = psycopg2.connect(connection_string)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_connection_data(db_name=None):
    """
    Give back a properly formatted dictionary based on the environment variables values which are started
    with :MY__PSQL_: prefix
    :db_name: optional parameter. By default, it uses the environment variable value.
    """
    if db_name is None:
        db_name = os.environ.get('MY_PSQL_DBNAME')

    return {
        'dbname': db_name,
        'user': os.environ.get('MY_PSQL_USER'),
        'host': os.environ.get('MY_PSQL_HOST'),
        'password': os.environ.get('MY_PSQL_PASSWORD')
    }


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


def get_connection_string():
    user_name = os.environ.get('MY_PSQL_USER')
    password = os.environ.get('MY_PSQL_PASSWORD')
    host = os.environ.get('MY_PSQL_HOST')
    database_name = os.environ.get('MY_PSQL_DBNAME')
    env_variables_defined = user_name and password and host and database_name
    if env_variables_defined:
        return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
    else:
        raise KeyError('Some necessary environment variable(s) are not defined')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = establish_connection()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper


def is_logged(session):
    alert = True
    if 'username' in session:
        alert = False
    return alert


def user_registration(username, password):
    password = hash_password(password)
    username_exists = queries.check_if_user_exist(username)
    if not username_exists:
        queries.add_new_user_to_db(username, password)
        return username_exists
    else:
        return username_exists


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


#
#
# import os
# import psycopg2
# import psycopg2.extras
# import queries
# import bcrypt
#
#
# def establish_connection(connection_data=None):
#     """
#     Create a database connection based on the :connection_data: parameter
#     :connection_data: Connection string attributes
#     :returns: psycopg2.connection
#     """
#     if connection_data is None:
#         connection_data = get_connection_data()
#     try:
#         connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
#                                                                      connection_data['user'],
#                                                                      connection_data['host'],
#                                                                      connection_data['password'])
#         conn = psycopg2.connect(connect_str)
#         conn.autocommit = True
#     except psycopg2.DatabaseError as e:
#         print("Cannot connect to database.")
#         print(e)
#     else:
#         return conn
#
#
# def get_connection_data(db_name=None):
#     """
#     Give back a properly formatted dictionary based on the environment variables values which are started
#     with :MY__PSQL_: prefix
#     :db_name: optional parameter. By default, it uses the environment variable value.
#     """
#     if db_name is None:
#         db_name = os.environ.get('MY_PSQL_DBNAME')
#
#     return {
#         'dbname': db_name,
#         'user': os.environ.get('MY_PSQL_USER'),
#         'host': os.environ.get('MY_PSQL_HOST'),
#         'password': os.environ.get('MY_PSQL_PASSWORD')
#     }
#
#
# def execute_select(statement, variables=None, fetchall=True):
#     """
#     Execute SELECT statement optionally parameterized.
#     Use fetchall=False to get back one value (fetchone)
#
#     Example:
#     > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})
#     statement: SELECT statement
#     variables:  optional parameter dict, optional parameter fetchall"""
#     result_set = []
#     with establish_connection() as conn:
#         with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
#             cursor.execute(statement, variables)
#             result_set = cursor.fetchall() if fetchall else cursor.fetchone()
#     return result_set
#
#
# def get_connection_string():
#     user_name = os.environ.get('MY_PSQL_USER')
#     password = os.environ.get('MY_PSQL_PASSWORD')
#     host = os.environ.get('MY_PSQL_HOST')
#     database_name = os.environ.get('MY_PSQL_DBNAME')
#     env_variables_defined = user_name and password and host and database_name
#     if env_variables_defined:
#         return 'postgresql://{user_name}:{password}@{host}/{database_name}'.format(
#             user_name=user_name,
#             password=password,
#             host=host,
#             database_name=database_name
#         )
#     else:
#         raise KeyError('Some necessary environment variable(s) are not defined')
#
#
# def open_database():
#     try:
#         connection_string = get_connection_string()
#         connection = psycopg2.connect(connection_string)
#         connection.autocommit = True
#     except psycopg2.DatabaseError as exception:
#         print('Database connection problem')
#         raise exception
#     return connection
#
#
# def connection_handler(function):
#     def wrapper(*args, **kwargs):
#         connection = open_database()
#         dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#         ret_value = function(dict_cur, *args, **kwargs)
#         dict_cur.close()
#         connection.close()
#         return ret_value
#     return wrapper
#
#
# def is_logged(session):
#     alert = True
#     if 'username' in session:
#         alert = False
#     return alert
#
#
# def user_registration(username, password):
#     password = hash_password(password)
#     username_exists = queries.check_if_user_exist(username)
#     if not username_exists:
#         queries.add_new_user_to_db(username, password)
#         return username_exists
#     else:
#         return username_exists
#
#
# def hash_password(plain_text_password):
#     hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
#     return hashed_bytes.decode('utf-8')
#
#
# def verify_password(plain_text_password, hashed_password):
#     hashed_bytes_password = hashed_password.encode('utf-8')
#     return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)
