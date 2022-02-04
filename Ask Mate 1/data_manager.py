import time
import connection
import server


def list_prepare_question_to_show():
    headers = ["submission_time", "view_number", "vote_number", "title", "message"]
    data = connection.read_file(server.question_path())
    data = connection.timestamp_to_date(data)
    slice_message(data)
    data_sorted_by_id = sorted(data, key=lambda d: d['id'], reverse=True)
    data = data_sorted_by_id
    return headers, data


def slice_message(data):
    for element in data:
        if len(str(element['message'])) > 100:
            element['message'] = element['message'][:97]+'...'


def list_sort_question(data, order, direction):
    connection.sort_data(data, order, direction)


def question_display_by_id_with_answers(question_id):
    answers = connection.get_answers_by_id(question_id)
    connection.sort_by_votes(answers)
    for answer in answers:
        answer.pop('question_id', None)
    question = connection.get_data_by_id(server.question_path(), question_id)
    question['view_number'] = str(int(question['view_number']) + 1)
    final_data = connection.edit_data(question_id, question, server.question_path())
    connection.data_writer(server.question_path(), final_data, server.QUESTION_TITLE)
    question = connection.timestamp_to_date(question)
    answers = connection.timestamp_to_date(answers)
    return question, answers


def add_question_to_file(title, question, image):
    submission_time = time.time()
    image_path = server.upload_image(image)
    question_id = connection.add_question_to_file(title, question, submission_time, image_path)
    return question_id


def add_answer_to_file(question_id, message, image):
    adding_answer = {'id': connection.create_new_id(server.answer_path()), 'submission_time': time.time(),
                     'vote_number': 0, 'question_id': question_id, 'message': message}
    image_path = server.upload_image(image)
    adding_answer['image'] = image_path
    connection.write_new_answer_to_file(adding_answer)


def edit_question_pass_data_to_file(question_id, edited_title, edited_question):
    new_submission_time = time.time()
    connection.edit_question_in_file(question_id, edited_title, edited_question, new_submission_time)
