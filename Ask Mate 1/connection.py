import csv
import server
import os
from datetime import datetime


# append new answer to answer.csv
def write_new_answer_to_file(new_answer):
    with open(server.answer_path(), 'a', newline='\n') as csvfile:
        fieldnames = server.ANSWER_TITLE
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': new_answer['id'], 'submission_time': new_answer['submission_time'],
                         'vote_number': new_answer['vote_number'], 'question_id': new_answer['question_id'],
                         'message': new_answer['message'], 'image': new_answer['image']})


# creates new id for questions and answers
def create_new_id(file):
    data_list = read_file(file)
    new_id = len(data_list) + 1
    return new_id


# append question to question.csv
def add_question_to_file(title, question, submission_time, image):
    file = server.question_path()
    new_id = create_new_id(file)
    view_number = 0
    vote_number = 0
    with open(server.question_path(), 'a', newline='\n') as csvfile:
        fieldnames = server.QUESTION_TITLE
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': new_id, 'submission_time': submission_time, 'view_number': view_number,
                         'vote_number': vote_number, 'title': title, 'message': question, 'image': image})
    return new_id


# delete item from list by question id
def delete_item_from_list(data_id, data_list):
    list_updated = []
    for item in data_list:
        if item['id'] == data_id:
            try:
                os.remove(f"static/uploads/{item['image']}")
            except:
                pass
            if len(item) == server.ANSWER_DATABASE_LENGTH:
                question_id = item['question_id']
            continue
        else:
            list_updated.append(item)
    if len(data_list[0]) == server.ANSWER_DATABASE_LENGTH:
        return list_updated, question_id
    else:
        return list_updated


# delete item from answers by question id
def delete_item_from_answers(data_id, data_list):
    list_updated = []
    for item in data_list:
        if item['question_id'] == data_id:
            try:
                os.remove(f"static/uploads/{item['image']}")
            except:
                pass
        else:
            list_updated.append(item)
    return list_updated


# delete from answer or question from file and return question id if deleted answer
def delete_from_file(data_id, file_questions, file_answers):
    question_list = read_file(file_questions)
    answer_list = read_file(file_answers)
    if len(question_list[0]) == server.ANSWER_DATABASE_LENGTH:
        question_list_updated, question_id = delete_item_from_list(data_id, question_list)
    else:
        question_list_updated = delete_item_from_list(data_id, question_list)
        answer_list_updated = delete_item_from_answers(data_id, answer_list)
        update_file(file_questions, question_list_updated)
        update_answers_question_id(file_answers, answer_list_updated, data_id)
    if len(question_list[0]) == server.ANSWER_DATABASE_LENGTH:
        return question_id


# delete answer from file
def delete_answer_from_file(data_id, file):
    data_list = read_file(file)
    if len(data_list[0]) == server.ANSWER_DATABASE_LENGTH:
        list_updated, question_id = delete_item_from_list(data_id, data_list)
    else:
        list_updated = delete_item_from_list(data_id, data_list)
    update_file(file, list_updated)
    if len(data_list[0]) == server.ANSWER_DATABASE_LENGTH:
        return question_id


# update question and answers id after deletion
def update_answers_question_id(file, list_updated, data_id):
    with open(file, 'w', newline='\n') as csvfile:
        if len(list_updated) > 0:
            fieldnames = server.ANSWER_TITLE
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in list_updated:
                if item['question_id'] >= data_id:
                    writer.writerow({'id': item['id'], 'submission_time': item['submission_time'],
                                     'vote_number': item['vote_number'], 'question_id': str(int(item['question_id']) - 1),
                                     'message': item['message'], 'image': item['image']})
                else:
                    writer.writerow({'id': item['id'], 'submission_time': item['submission_time'],
                                     'vote_number': item['vote_number'],
                                     'question_id': item['question_id'],
                                     'message': item['message'], 'image': item['image']})
        else:
            fieldnames = server.ANSWER_TITLE
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


# update file after deletion
def update_file(file, list_updated):
    with open(file, 'w', newline='\n') as csvfile:
        if len(list_updated) > 0:
            if len(list_updated[0]) == server.QUESTION_DATABASE_LENGTH:
                fieldnames = server.QUESTION_TITLE
            elif len(list_updated[0]) == server.ANSWER_DATABASE_LENGTH:
                fieldnames = server.ANSWER_TITLE
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            counter = 1
            for item in list_updated:
                if len(list_updated[0]) == server.QUESTION_DATABASE_LENGTH:
                    writer.writerow(
                        {'id': counter, 'submission_time': item['submission_time'], 'view_number': item['view_number'],
                         'vote_number': item['vote_number'], 'title': item['title'], 'message': item['message'],
                         'image': item['image']})
                if len(list_updated[0]) == server.ANSWER_DATABASE_LENGTH:
                    writer.writerow({'id': counter, 'submission_time': item['submission_time'],
                                     'vote_number': item['vote_number'], 'question_id': item['question_id'],
                                     'message': item['message'], 'image': item['image']})
                counter += 1
        else:
            if file == server.question_path():
                fieldnames = server.QUESTION_TITLE
            elif file == server.answer_path():
                fieldnames = server.ANSWER_TITLE
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


# get path to file
def get_path(filename: str):
    return os.path.join(os.path.dirname(__file__), filename)


# read file and return dict
def read_file(filename):
    file = get_path(filename)
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)


# convert timestamp to date format
def timestamp_to_date(dictionary):
    if type(dictionary) is dict:
        dictionary['submission_time'] = dictionary['submission_time'].split('.')
        dictionary['submission_time'] = datetime.fromtimestamp(int(dictionary['submission_time'][0]))
    if type(dictionary) is list:
        for one_dict in dictionary:
            one_dict['submission_time'] = one_dict['submission_time'].split('.')
            one_dict['submission_time'] = datetime.fromtimestamp(int(one_dict['submission_time'][0]))
    return dictionary


# get question to edit by id ket
def get_question_to_edit(question_id):
    data_list = read_file(server.question_path())
    for item in data_list:
        if item['id'] == question_id:
            return item


# edit question in question.csv
def edit_question_in_file(question_id, edited_title, edited_question, new_submission_time):
    data_list = read_file(server.question_path())
    for item in data_list:
        if item['id'] == question_id:
            item['submission_time'] = new_submission_time
            item['title'] = edited_title
            item['message'] = edited_question
    update_file(server.question_path(), data_list)


# change vote number
def vote(file, data_id, vote):
    data_list = read_file(file)
    question_id = ""
    for item in data_list:
        if item['id'] == data_id:
            if len(data_list[0]) == server.ANSWER_DATABASE_LENGTH:
                question_id = item['question_id']
                question_list = vote_dont_change_view(data_list, item, question_id)
            else:
                data_list = vote_dont_change_view(data_list, item, question_id)
            new_vote_number = int(item['vote_number'])
            if vote == '+':
                new_vote_number += 1
            elif vote == '-':
                new_vote_number -= 1
            item['vote_number'] = str(new_vote_number)
            break
    update_file(file, data_list)
    if len(data_list[0]) == server.ANSWER_DATABASE_LENGTH:
        update_file(server.question_path(), question_list)
        return question_id


# don't change view count after voting
def vote_dont_change_view(data_list, item, question_id):
    if len(data_list[0]) == server.QUESTION_DATABASE_LENGTH:
        new_view_number = int(item['view_number'])
        new_view_number -= 1
        item['view_number'] = str(new_view_number)
        return data_list
    else:
        question_list = read_file(server.question_path())
        for element in question_list:
            if element['id'] == question_id:
                new_view_number = int(element['view_number'])
                new_view_number -= 1
                element['view_number'] = str(new_view_number)
                return question_list


# sort list function
def sort_data(data, order_by, order_direction):
    if order_direction == "from lowest":
        direction = False
    elif order_direction == "from highest":
        direction = True
    elif order_direction == None:
        direction = False

    if order_by == "Number of votes":
        data.sort(key=lambda x: int(x["vote_number"]), reverse=direction)
    elif order_by == 'Submission time':
        data.sort(key=lambda x: x['submission_time'], reverse=direction)
    elif order_by == 'Title':
        data.sort(key=lambda x: x["title"], reverse=direction)
    elif order_by == 'Message':
        data.sort(key=lambda x: x["message"], reverse=direction)
    elif order_by == 'Number of views':
        data.sort(key=lambda x: int(x["view_number"]), reverse=direction)
    return data


def get_all_data(filename):
    with open(filename, "r") as data_file:
        reader = csv.DictReader(data_file)
        return [*reader]


def get_data_by_id(filename, id_):
    list_of_data = get_all_data(filename)
    for row in list_of_data:
        if row['id'] == id_:
            return row


def get_answers_by_id(id_):
    list_of_answers = get_all_data(server.answer_path())
    return [answer for answer in list_of_answers if answer['question_id'] == id_]


def sort_by_votes(answers):
    sort_data(answers, "Number of votes", "from highest")


def data_writer(filename, to_write, fieldnames):
    with open(filename, "w") as file_to_write:
        writer = csv.DictWriter(file_to_write, fieldnames)
        writer.writeheader()
        for row in to_write:
            writer.writerow(row)


def edit_data(id_, new_line, filename):
    list_of_data = get_all_data(filename)
    for i, row in enumerate(list_of_data):
        if row["id"] == id_:
            list_of_data[i] = new_line
    return list_of_data


def get_title_by_id(question_id):
    dicts = read_file(server.question_path())
    for dict in dicts:
        if dict['id'] == question_id:
            return dict['title']
