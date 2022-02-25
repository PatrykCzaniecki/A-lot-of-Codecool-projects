import datetime

import connection
import server


def list_prepare_question_to_show():
    headers = ["submission_time", "view_number", "vote_number", "title", "message"]
    data = connection.get_data_questions_sort_by_id()
    return headers, data


def slice_message(data):
    for element in data:
        if len(str(element['message'])) > 100:
            element['message'] = element['message'][:97] + '...'


def list_sort_question(data, order, direction):
    connection.sort_data(data, order, direction)


def question_display_by_id_with_answers(question_id):
    question = connection.get_data_question_with_id(question_id)
    answers = connection.get_data_answers_sort_by_vote_number(question_id)
    comments_to_questions = connection.get_data_comments(question_id)
    return question, answers, comments_to_questions


def get_comments_for_answers(list_with_answer_id):
    list_with_comments = []
    for answer_id in list_with_answer_id:
        comments_to_answers = connection.get_comments_for_answers(answer_id)
        list_with_comments.append(comments_to_answers)
    return list_with_comments


def add_question_to_file(title, question, image):
    submission_time = datetime.datetime.now()
    image_path = server.upload_image(image)
    connection.add_question_to_db(title, question, submission_time, image_path)
    question_id = connection.get_id(submission_time)
    return question_id


def add_answer_to_file(question_id, message, image):
    submission_time = datetime.datetime.now()
    image_path = server.upload_image(image)
    connection.add_answer_to_db(question_id, message, submission_time, image_path)


def get_tags_for_question(question_id):
    tags_id_for_question = connection.get_tags_ids_for_question(question_id)
    tags = []
    for id in tags_id_for_question:
        tags.append(connection.get_tag_by_id(id))
    return tags


def add_new_defined_tags(new_defined_tags, question_id):
    is_not_duplicate = True
    existing_tags = connection.get_all_existing_tags()
    existing_tags_list = []
    for tags in existing_tags:
        existing_tags_list.append(tags['name'])
    print(existing_tags_list)
    if ',' in new_defined_tags:
        new_defined_tags = new_defined_tags.split(',')
        for tag in new_defined_tags:
            tag = tag.strip()
            if tag != '' and tag not in existing_tags_list:
                connection.add_new_defined_tags_to_db(tag)
                tag_id = connection.get_id_by_tag(tag)
                connection.apply_tag_to_question(question_id, tag_id)
    else:
        new_defined_tags = new_defined_tags.strip()
        if new_defined_tags != '' and new_defined_tags not in existing_tags_list:
            connection.add_new_defined_tags_to_db(new_defined_tags)
            tag_id = connection.get_id_by_tag(new_defined_tags)
            connection.apply_tag_to_question(question_id, tag_id)


def add_comment_to_question(question_id, message):
    submission_time = datetime.datetime.now()
    edited_count = 0
    connection.add_comment_to_question(question_id, message, submission_time, edited_count)


def add_comment_to_answer(answer_id, message):
    submission_time = datetime.datetime.now()
    edited_count = 0
    connection.add_comment_to_answer(answer_id, message, submission_time, edited_count)


def add_answer_to_file(question_id, message, image):
    submission_time = datetime.datetime.now()
    image_path = server.upload_image(image)
    connection.add_answer_to_db(question_id, message, submission_time, image_path)
