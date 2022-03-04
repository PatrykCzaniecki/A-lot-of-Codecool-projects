import database_common
import server


@database_common.connection_handler
def delete_from_db(cursor, db_name, db_where, db_var):
    query = """
        DELETE FROM %s
        WHERE %s = '%s'""" % (db_name, db_where, db_var)
    cursor.execute(query)


@database_common.connection_handler
def get_images_by_id(cursor, db_name, id):
    query = """
        SELECT image
        FROM %s
        WHERE id = '%s'""" % (db_name, id)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_questions_sort_by_id(cursor):
    query = """
        SELECT question.id, submission_time, view_number, vote_number, title, message, image, users.name
        FROM question
        INNER JOIN users
        ON question.user_id = users.id
        ORDER BY question.id DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_question_with_id(cursor, question_id):
    query = """
        SELECT question.*, u.name
        FROM question
        INNER JOIN users u on question.user_id = u.id
        WHERE question.id = %s
        ORDER BY question.id""" % (question_id)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_answers_sort_by_vote_number(cursor, question_id):
    query = """
        SELECT answer.*, u.name
        FROM answer
        INNER JOIN users u on answer.user_id = u.id
        WHERE question_id = '%s'
        ORDER BY vote_number DESC""" % (question_id)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_data_comments(cursor, id):
    query = """
        SELECT comment.*, u.name
        FROM comment
        INNER JOIN users u on u.id = comment.user_id
        WHERE question_id = '%s'""" % (id)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def add_question_to_db(cursor, title, question, submission_time, image_path, user_id):
    query = """
        INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id)
        VALUES ('%s','%s','%s','%s','%s','%s', '%s')""" % (submission_time, 0, 0, title, question, image_path, user_id)
    cursor.execute(query)


@database_common.connection_handler
def add_answer_to_db(cursor, question_id, message, submission_time, image_path, user_id):
    query = """
        INSERT INTO answer (submission_time, vote_number, question_id, message, image, user_id)
        VALUES ('%s','%s','%s','%s','%s', '%s')""" % (submission_time, 0, question_id, message, image_path, user_id)
    cursor.execute(query)


@database_common.connection_handler
def add_comment_to_question(cursor, question_id, message, submission_time, edited_count, user_id):
    query = """
        INSERT INTO comment (question_id, message, submission_time, edited_count, user_id)
        VALUES ('%s','%s','%s','%s', '%s')""" % (question_id, message, submission_time, 0, user_id)
    cursor.execute(query)


@database_common.connection_handler
def add_comment_to_answer(cursor, answer_id, message, submission_time, edited_count, user_id):
    query = """
        INSERT INTO comment (answer_id, message, submission_time, edited_count, user_id)
        VALUES ('%s','%s','%s','%s', '%s')""" % (answer_id, message, submission_time, 0, user_id)
    cursor.execute(query)


@database_common.connection_handler
def change_value_db(cursor, db_name, db_col, mark, db_where, db_where_equal):
    query = """
        UPDATE %s
        SET %s = %s %s 1
        WHERE %s = '%s'""" % (db_name, db_col, db_col, mark, db_where, db_where_equal)
    cursor.execute(query)


@database_common.connection_handler
def get_answer_id_connected_to_question(cursor, question_id):
    query = """
        SELECT id 
        FROM answer
        WHERE question_id = '%s'""" % (question_id)
    cursor.execute(query)
    lists = cursor.fetchall()
    list_to_return = [list['id'] for list in lists]
    return list_to_return


@database_common.connection_handler
def get_id(cursor, submission_time):
    query = """
        SELECT id FROM question
        WHERE submission_time = '%s'""" % (submission_time)
    cursor.execute(query)
    id = cursor.fetchall()
    id = list_of_dicts_to_str('id', id)
    return id


@database_common.connection_handler
def get_question_to_edit(cursor, question_id):
    query = """
        SELECT * FROM question
        WHERE id = '%s'""" % (question_id)
    cursor.execute(query)
    question = cursor.fetchall()
    question = question[0]
    return question


@database_common.connection_handler
def update_question(cursor, question_id, edited_title, edited_question):
    query = """
        UPDATE question
        SET title = '%s', message = '%s'
        WHERE id = '%s'""" % (edited_title, edited_question, question_id)
    cursor.execute(query)


@database_common.connection_handler
def get_answer_to_edit(cursor, answer_id):
    query = """
        SELECT * FROM answer
        WHERE id = '%s'""" % (answer_id)
    cursor.execute(query)
    answer = cursor.fetchall()
    answer = answer[0]
    return answer


@database_common.connection_handler
def check_if_user_exist(cursor, username):
    query = """
        SELECT name FROM users WHERE name=%s
        """
    cursor.execute(query, (username,))
    is_exist = cursor.fetchall()
    if len(is_exist) > 0:
        is_exist = True
    else:
        is_exist = False
    return is_exist


@database_common.connection_handler
def add_new_user_to_db(cursor, username, password, registration_date):
    query = """
        INSERT INTO users (name, password,registration_date)
        VALUES (%s,%s,%s)
        """
    cursor.execute(query, (username, password, registration_date))


@database_common.connection_handler
def update_answer(cursor, answer_id, edited_answer):
    query = """
        UPDATE answer
        SET message = '%s'
        WHERE id = '%s'""" % (edited_answer, answer_id)
    cursor.execute(query)


@database_common.connection_handler
def get_comment_to_edit(cursor, comment_id):
    query = """
        SELECT * FROM comment
        WHERE id = '%s'""" % (comment_id)
    cursor.execute(query)
    comment = cursor.fetchall()
    comment = comment[0]
    return comment


@database_common.connection_handler
def update_comment(cursor, comment_id, edited_comment):
    query = """
        UPDATE comment
        SET message = '%s'
        WHERE id = '%s'""" % (edited_comment, comment_id)
    cursor.execute(query)


@database_common.connection_handler
def get_from_db(cursor, db_select, db_name, db_where, db_var):
    query = """
        SELECT %s
        FROM %s
        WHERE %s = %s""" % (db_select, db_name, db_where, db_var)
    cursor.execute(query)
    var = cursor.fetchall()
    var = list_of_dicts_to_str(str(db_select), var)
    return var


@database_common.connection_handler
def get_comments_for_answers(cursor, answer_id):
    query = """
        SELECT comment.*, u.name
        FROM comment
        INNER JOIN users u on u.id = comment.user_id
        WHERE answer_id = %s""" % (answer_id)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_title_by_id(cursor, question_id):
    query = """
        SELECT title FROM question
        WHERE id = '%s'""" % (question_id)
    cursor.execute(query)
    title = cursor.fetchall()
    title = list_of_dicts_to_str('title', title)
    return title


@database_common.connection_handler
def get_all_existing_tags(cursor):
    query = """
        SELECT name 
        FROM tag
        ORDER BY name"""
    cursor.execute(query)
    return cursor.fetchall()


def list_of_dicts_to_str(key, list):
    list = list[0]
    string = list[key]
    return string


def convert_order(order):
    if order == "from lowest":
        return 'ASC'
    elif order == "from highest":
        return 'DESC'


def convert_direction(direction):
    if direction == "Number of votes":
        return 'vote_number'
    elif direction == 'Submission time':
        return 'submission_time'
    elif direction == 'Title':
        return 'title'
    elif direction == 'Message':
        return 'message'
    elif direction == 'Number of views':
        return 'view_number'


@database_common.connection_handler
def sort_questions(cursor, direction, order):
    order = convert_order(order)
    direction = convert_direction(direction)
    query = """
            SELECT question.id, submission_time, view_number, vote_number, title, message, image, users.name
            FROM question
            INNER JOIN users
            ON question.user_id = users.id
            ORDER BY %s %s""" % (direction, order)
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_tags_ids_for_question(cursor, question_id):
    query = """
            SELECT tag_id
            FROM question_tag
            WHERE question_id = %s""" % (question_id)
    cursor.execute(query)
    ids = cursor.fetchall()
    list_id = []
    for id in ids:
        list_id.append(id['tag_id'])
    return list_id


@database_common.connection_handler
def get_tag_by_id(cursor, id):
    query = """
        SELECT name
        FROM tag
        WHERE id = '%s'""" % (id)
    cursor.execute(query)
    tag = cursor.fetchall()
    tag = tag[0]
    tag_to_return = tag['name']
    return tag_to_return


@database_common.connection_handler
def get_id_by_tag(cursor, tag):
    query = """
        SELECT id
        FROM tag
        WHERE name = '%s'""" % (tag)
    cursor.execute(query)
    id = cursor.fetchall()
    id = id[0]
    id_to_return = id['id']
    return id_to_return


@database_common.connection_handler
def apply_tag_to_question(cursor, question_id, tag_id):
    query = """
        INSERT INTO question_tag (question_id,tag_id)
        VALUES (%s,%s)
        ON CONFLICT DO NOTHING""" % (question_id, tag_id)
    cursor.execute(query)


@database_common.connection_handler
def delete_tag_from_question(cursor, question_id, tag_id):
    query = """
        DELETE FROM question_tag
        WHERE question_id = '%s' AND tag_id = '%s'""" % (question_id, tag_id)
    cursor.execute(query)


@database_common.connection_handler
def add_new_defined_tags_to_db(cursor, new_defined_tags):
    query = """
        INSERT INTO tag (name)
        VALUES ('%s')""" % (new_defined_tags)
    cursor.execute(query)


@database_common.connection_handler
def search_in_question_message(cursor, searched_phrase):
    searched_phrase_in_any_position = "%" + searched_phrase + "%"
    query_message = """
        SELECT *
        FROM question
        WHERE LOWER(message) LIKE LOWER('%s')""" % (searched_phrase_in_any_position,)
    cursor.execute(query_message)
    return cursor.fetchall()


@database_common.connection_handler
def search_in_question_title(cursor, searched_phrase):
    searched_phrase_in_any_position = "%" + searched_phrase + "%"
    query_title = """
        SELECT *
        FROM question
        WHERE LOWER(title) LIKE LOWER('%s')""" % (searched_phrase_in_any_position,)
    cursor.execute(query_title)
    return cursor.fetchall()


def search_in_question(searched_phrase):
    searched_in_title = search_in_question_title(searched_phrase)
    searched_in_message = search_in_question_message(searched_phrase)
    searched_in_questions = [data for data in searched_in_message if data not in searched_in_title]
    for data in searched_in_title:
        searched_in_questions.append(data)
    return searched_in_questions


@database_common.connection_handler
def search_in_answer(cursor, searched_phrase):
    searched_phrase_in_any_position = "%" + searched_phrase + "%"
    query = """
        SELECT *
        FROM answer
        WHERE LOWER(message) LIKE LOWER('%s')""" % (searched_phrase_in_any_position,)
    cursor.execute(query)
    searched_answers = cursor.fetchall()
    list_of_id = [question_id['question_id'] for question_id in searched_answers]
    return list_of_id, searched_answers


def check_for_duplicated(questions):
    list = []
    for question in questions:
        if question not in list:
            list.append(question)
    return list


@database_common.connection_handler
def get_all_questions_of_specific_id(cursor, searched_phrase):
    list_of_id, searched_answers = search_in_answer(searched_phrase)
    questions = []
    for question_id in list_of_id:
        query = """
            SELECT *
            FROM question
            WHERE id = '%s'""" % (question_id,)
        cursor.execute(query)
        question = cursor.fetchall()
        question = question[0]
        questions.append(question)
    questions = check_for_duplicated(questions)
    return questions, searched_answers


def search_in_questions_and_answers(searched_phrase):
    searched_in_question = search_in_question(searched_phrase)
    searched_in_answer, searched_answers = get_all_questions_of_specific_id(searched_phrase)
    searched_questions = [question for question in searched_in_question if question not in searched_in_answer]
    for question in searched_in_answer:
        searched_questions.append(question)
    return searched_questions, searched_answers


def mark_searched_phrase(all_searched_questions, searched_phrase):  # W js
    all_searched_questions_to_return = []
    for question in all_searched_questions:
        question_dict = {}
        question_dict['id'] = question['id']
        question_dict['submission_time'] = question['submission_time']
        question_dict['view_number'] = question['view_number']
        question_dict['vote_number'] = question['vote_number']
        question_dict['image'] = question['image']
        if searched_phrase.lower() in question['message'].lower():
            message = str(question['message'])
            index = message.lower().find(searched_phrase.lower())
            message = message.lower().replace(searched_phrase.lower(),
                                              "<mark>" + message[index:index + len(searched_phrase)] + "</mark>")
            question_dict['message'] = message
        else:
            question_dict['message'] = question['message']
        if searched_phrase.lower() in question['title'].lower():
            title = str(question['title'])
            index = title.lower().find(searched_phrase.lower())
            title = title.lower().replace(searched_phrase.lower(),
                                          "<mark>" + title[index:index + len(searched_phrase)] + "</mark>")
            question_dict['title'] = title
        else:
            question_dict['title'] = question['title']
        all_searched_questions_to_return.append(question_dict)

    return all_searched_questions_to_return


def mark_searched_phrase_in_answers(searched_answers, searched_phrase):
    searched_answers_to_return = []
    for question in searched_answers:
        question_dict = {}
        question_dict['id'] = question['id']
        question_dict['submission_time'] = question['submission_time']
        question_dict['question_id'] = question['question_id']
        question_dict['vote_number'] = question['vote_number']
        question_dict['image'] = question['image']
        if searched_phrase.lower() in question['message'].lower():
            message = str(question['message'])
            index = message.lower().find(searched_phrase.lower())
            message = message.lower().replace(searched_phrase.lower(),
                                              "<mark>" + message[index:index + len(searched_phrase)] + "</mark>")
            question_dict['message'] = message
        else:
            question_dict['message'] = question['message']
        searched_answers_to_return.append(question_dict)

    return searched_answers_to_return


@database_common.connection_handler
def get_all_users_data(cursor):
    query = """
        SELECT *
        FROM users
        ORDER BY id"""
    cursor.execute(query)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def username_exists(cursor, username):
    query = """
        SELECT name FROM users """
    cursor.execute(query)
    list_of_all_user_names = [user['name'] for user in cursor.fetchall()]
    return username in list_of_all_user_names


@database_common.connection_handler
def get_password(cursor, username):
    query = """
        SELECT password FROM users
        WHERE name = '%s'""" % (username)
    cursor.execute(query)
    password = cursor.fetchone()
    return password['password']


@database_common.connection_handler
def get_user_data_by_id(cursor, user_id):
    query = """
        SELECT users.id, users.name, registration_date, reputation
        FROM users    
        WHERE users.id=%s
        """
    cursor.execute(query, (user_id,))
    return cursor.fetchone()


@database_common.connection_handler
def get_number_of_questions_by_user_id(cursor, user_id):
    query = """
        SELECT COUNT(id)
        FROM question    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    count = cursor.fetchone()
    return count['count']


@database_common.connection_handler
def get_number_of_answers_by_user_id(cursor, user_id):
    query = """
        SELECT COUNT(id)
        FROM answer    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    count = cursor.fetchone()
    return count['count']


@database_common.connection_handler
def get_number_of_comments_by_user_id(cursor, user_id):
    query = """
        SELECT COUNT(id)
        FROM comment    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    count = cursor.fetchone()
    return count['count']


@database_common.connection_handler
def get_user_questions(cursor, user_id):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


@database_common.connection_handler
def get_user_answers(cursor, user_id):
    query = """
        SELECT id, submission_time, vote_number, question_id, message, accepted
        FROM answer    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


@database_common.connection_handler
def get_user_id_by_name(cursor, username):
    query = """
        SELECT id
        FROM users    
        WHERE name=%s
        """
    cursor.execute(query, (username,))
    user_id = cursor.fetchone()
    return user_id['id']


@database_common.connection_handler
def get_user_comments(cursor, user_id):
    query = """
        SELECT question_id, answer_id, message, submission_time, edited_count
        FROM comment    
        WHERE user_id=%s
        """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


@database_common.connection_handler
def get_user_id_by_other_id(cursor, question_id, table):
    query = """
            SELECT user_id
            FROM %s
            WHERE id=%s
            """ % (table, question_id)
    cursor.execute(query)
    creator_id = cursor.fetchone()
    return creator_id['user_id']


@database_common.connection_handler
def get_all_tags_data(cursor):
    query = """
        SELECT *
        FROM tag
        ORDER BY id"""
    cursor.execute(query)
    data = cursor.fetchall()
    return data


@database_common.connection_handler
def get_number_of_marked_questions_by_tag_id(cursor, tag_id):
    query = """
        SELECT COUNT(tag_id)
        FROM question_tag    
        WHERE tag_id=%s
        """
    cursor.execute(query, (tag_id,))
    count = cursor.fetchone()
    return count['count']


@database_common.connection_handler
def accept_answer(cursor, answer_id):
    query = """
        UPDATE answer
        SET accepted = 1
        WHERE id = %s""" % (answer_id, )
    cursor.execute(query)


@database_common.connection_handler
def change_reputation(cursor, sign, number, user_id):
    query = """
            UPDATE users
            SET reputation = reputation %s %s
            WHERE id = %s""" % (sign, number, user_id)
    cursor.execute(query)


@database_common.connection_handler
def dont_accept_answer(cursor, answer_id):
    query = """
        UPDATE answer
        SET accepted = 0
        WHERE id = %s""" % (answer_id, )
    cursor.execute(query)
