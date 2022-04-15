import data_manager
from psycopg2 import sql
import main


def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    status = data_manager.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;"""
        , {"status_id": status_id})
    return status


def get_last_id ():
    last_id = data_manager.execute_select(
        """
        SELECT MAX(ID) FROM boards
        ;"""
    )
    return last_id


def get_boards():
    """
    Gather all boards
    :return:
    """
    return data_manager.execute_select(
        """
        SELECT boards.id, boards.title, private, user_id, COUNT(s.id) AS statuses FROM boards
        LEFT JOIN statuses s on boards.id = s.board_id
        WHERE private = 0
        GROUP BY boards.id
        ORDER BY boards.id
        ;""")


def get_private_boards(user_id):
    """
    Gather all boards
    :return:
    """
    all_private_boards = data_manager.execute_select(
        """
        SELECT boards.id, boards.title, private, user_id, COUNT(s.id) AS statuses FROM boards
        LEFT JOIN statuses s on boards.id = s.board_id
        WHERE private = 1 AND user_id = %(user_id)s
        GROUP BY boards.id
        ORDER BY boards.id
        ;"""
        , {"user_id": user_id})
    return all_private_boards


def get_cards_for_board(board_id):
    matching_cards = data_manager.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ORDER BY card_order;
        ;"""
        , {"board_id": board_id})
    return matching_cards


def get_all_columns_names(board_id):
    columns = data_manager.execute_select(
        """
        SELECT * 
        FROM statuses
        WHERE board_id = %(board_id)s
        ORDER BY id
        ;"""
        , {"board_id": board_id})
    return columns


@data_manager.connection_handler
def rename_board_by_id(cursor, board_id, board_title):
    cursor.execute(
        sql.SQL("""
            UPDATE boards
            SET title = {board_title}
            WHERE id = {board_id}
        """).format(board_id=sql.Literal(board_id), board_title=sql.Literal(board_title))
    )


@data_manager.connection_handler
def rename_column_by_id(cursor, column_id, column_title):
    cursor.execute(
        sql.SQL("""
            UPDATE statuses
            SET title = {column_title}
            WHERE id = {column_id}
        """).format(column_id=sql.Literal(column_id), column_title=sql.Literal(column_title))
    )


@data_manager.connection_handler
def rename_card_by_id(cursor, card_id, card_title):
    cursor.execute(
        sql.SQL("""
            UPDATE cards
            SET title = {card_title}
            WHERE id = {card_id}
        """).format(card_id=sql.Literal(card_id), card_title=sql.Literal(card_title))
    )


@data_manager.connection_handler
def add_board(cursor, new_title):
    query = """
    INSERT INTO boards (title)
    VALUES (%s)
    """
    cursor.execute(query, (new_title,))


@data_manager.connection_handler
def delete_specific_card(cursor, card_id):
    cursor.execute(
        sql.SQL("""
            DELETE FROM cards 
            WHERE id = {card_id};
        """).format(card_id=sql.Literal(card_id), )
    )


@data_manager.connection_handler
def check_if_user_exist(cursor, username):
    query = """
        SELECT name FROM users WHERE name=%s"""
    cursor.execute(query, (username,))
    exist = cursor.fetchall()
    if len(exist) > 0:
        exist = True
    else:
        exist = False
    return exist


@data_manager.connection_handler
def add_new_user_to_db(cursor, username, password):
    query = """
        INSERT INTO users (name, password)
        VALUES (%s, %s)"""
    cursor.execute(query, (username, password))


@data_manager.connection_handler
def username_exists(cursor, username):
    query = """
        SELECT name FROM users """
    cursor.execute(query)
    all_users = [user['name'] for user in cursor.fetchall()]
    return username in all_users


@data_manager.connection_handler
def get_password(cursor, username):
    query = """
        SELECT password FROM users
        WHERE name = '%s'""" % (username)
    cursor.execute(query)
    password = cursor.fetchone()
    return password['password']


@data_manager.connection_handler
def get_user_id(cursor, username):
    query = """
        SELECT id
        FROM users    
        WHERE name=%s"""
    cursor.execute(query, (username,))
    user_id = cursor.fetchone()
    return user_id['id']


@data_manager.connection_handler
def add_new_card_to_board(cursor, card_title, board_id, status_id, card_number):
    query = """
        INSERT INTO cards (board_id, status_id, title, card_order)
        VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (board_id, status_id, card_title, card_number))


def get_card_order(board_id, status_id):
    card_number = data_manager.execute_select(
        """
        SELECT max(card_order) FROM cards 
        WHERE board_id = %(board_id)s 
        AND status_id = %(status_id)s
        ;"""
        , {"board_id": board_id,
            "status_id": status_id})
    return card_number


def get_all_new_card_data():
    return data_manager.execute_select(
        """
        SELECT * FROM cards
        ORDER BY id DESC
        LIMIT 1
        ;""")


@data_manager.connection_handler
def delete_all_cards_from_board(cursor, board_id):
    cursor.execute(
        sql.SQL("""
            DELETE FROM cards 
            WHERE board_id = {board_id};
        """).format(board_id=sql.Literal(board_id), )
    )


@data_manager.connection_handler
def delete_all_columns_from_board(cursor, board_id):
    cursor.execute(
        sql.SQL("""
                DELETE FROM statuses 
                WHERE board_id = {board_id};
            """).format(board_id=sql.Literal(board_id), )
    )


@data_manager.connection_handler
def delete_board(cursor, board_id):
    cursor.execute(
        sql.SQL("""
            DELETE FROM boards 
            WHERE id = {board_id};
        """).format(board_id=sql.Literal(board_id), )
    )


@data_manager.connection_handler
def add_column(cursor, board_id):
    cursor.execute(
        sql.SQL("""
            INSERT INTO statuses (title, board_id)
            VALUES ('new status', {board_id});
        """).format(board_id=sql.Literal(board_id), )
    )


def new_column_data():
    return data_manager.execute_select(
        """
        SELECT * FROM statuses
        ORDER BY id DESC
        LIMIT 1
        ;""")


def all_boards_ids():
    return data_manager.execute_select(
        """
        SELECT id FROM boards
        WHERE private = 0
        ORDER BY id ASC
        ;""")


def all_private_ids(user_id):
    ids = data_manager.execute_select(
        """
        SELECT id FROM boards
        WHERE private = 1 and user_id = %(user_id)s 
        ORDER BY id ASC
        ;""",
        {"user_id": user_id})
    return ids


@data_manager.connection_handler
def delete_all_cards_from_column(cursor, column_id):
    cursor.execute(
        sql.SQL("""
                DELETE FROM cards 
                WHERE status_id = {column_id};
            """).format(column_id=sql.Literal(column_id), )
    )


@data_manager.connection_handler
def delete_specific_column(cursor, column_id):
    cursor.execute(
        sql.SQL("""
                    DELETE FROM statuses 
                    WHERE id = {column_id};
                """).format(column_id=sql.Literal(column_id), )
    )


@data_manager.connection_handler
def newCardPos(cursor, col, card, boardID):
    query = """
               SELECT card_order FROM cards
               WHERE board_id=%s and status_id=%s
               ORDER by card_order DESC LIMIT 1
               """
    cursor.execute(query, (boardID, col))
    dict_order = cursor.fetchone()
    if dict_order is None:
        max_order = 1
    else:
        max_order = dict_order['card_order']
    query = """
            UPDATE
            cards
            SET
            status_id = %s,
            card_order = %s
            WHERE
            id = %s
    """
    cursor.execute(query, (col, max_order, card))


@data_manager.connection_handler
def swap_cards(cursor,card_1,card_2):
    query = """
           SELECT title From cards
           WHERE id=%s;
           """
    cursor.execute(query, (card_1,))
    card_1_dict = cursor.fetchone()

    card_1_title = (card_1_dict['title'])

    query = """
           SELECT title From cards
           WHERE id=%s;
           """
    cursor.execute(query, (card_2,))
    card_2_dict = cursor.fetchone()

    card_2_title = (card_2_dict['title'])

    query = """
            UPDATE
            cards
            SET
            title = %s
            WHERE id = %s;
            """
    cursor.execute(query, (card_2_title, card_1,))

    query = """
            UPDATE
            cards
            SET
            title = %s
            WHERE id = %s;
            """
    cursor.execute(query, (card_1_title, card_2,))


@data_manager.connection_handler
def create_new_private_board(cursor, title, user_id):
    query = """
        INSERT INTO boards (title, private, user_id)
        VALUES (%s, %s, %s);"""
    cursor.execute(query, (title, 1, user_id))


def get_lowest_status(board_id):
    lowest = data_manager.execute_select(
        """
        SELECT MIN(id) FROM statuses
        WHERE board_id = %(board_id)s
        ;"""
    , {"board_id": board_id})
    return lowest

    query = """
           UPDATE
           cards
           SET
           title = %s
           WHERE id = %s;
           """
    cursor.execute(query, (card_2_title, card_1,))

def get_board_and_status_id(card_id):
    data = data_manager.execute_select(
        """
        SELECT board_id, status_id FROM cards
        WHERE id = %(card_id)s
        ;"""
        , {"card_id": card_id})
    return data


@data_manager.connection_handler
def archive(cursor, user_id):
    query = """
        UPDATE cards
        SET archive = %s
        WHERE id = %s"""
    cursor.execute(query, ("true",user_id))

@data_manager.connection_handler
def unarchive(cursor, user_id):
    query = """
        UPDATE cards
        SET archive = %s
        WHERE id = %s"""
    cursor.execute(query, ("false",user_id))
