import os

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

import connection
import data_manager

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# allowed file extension for file uploads
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# upload image on server
def upload_image(image):
    if image.filename == '':
        image_path = 'no_image'
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_path = filename
    return image_path


# load home page
@app.route("/")
def home_page():
    headers, data_questions = data_manager.list_prepare_question_to_show()
    order = 'Submission time'
    direction = "from highest"
    data_questions = connection.sort_questions(order, direction)
    data_five_questions = data_questions[:5]
    searched_phrase = request.args.get("search-phrase")
    if searched_phrase:
        all_searched_questions, searched_answers = connection.search_in_questions_and_answers(searched_phrase)
        all_searched_questions = connection.mark_searched_phrase(all_searched_questions, searched_phrase)
        if len(searched_answers) > 0:
            searched_answers = connection.mark_searched_phrase_in_answers(searched_answers, searched_phrase)
        return render_template('search.html',
                               searched_phrase=searched_phrase, data=all_searched_questions, headers=headers,
                               searched_answers=searched_answers)
    return render_template('index.html', data=data_five_questions, headers=headers)


# load question list page
@app.route("/list")
def list_questions():
    headers, data_questions = data_manager.list_prepare_question_to_show()
    order = request.args.get('order_by')
    direction = request.args.get('order_direction')
    if order or direction:
        data_questions = connection.sort_questions(order, direction)
    return render_template('list.html', data=data_questions, headers=headers)


# load question detail page
@app.route('/question/<question_id>')
def question_display(question_id):
    connection.change_value_db('question', 'view_number', '+', 'id', question_id)
    question, answers, comments_to_questions = data_manager.question_display_by_id_with_answers(question_id)
    list_with_answer_id = []
    for answer in answers:
        list_with_answer_id.append(answer['id'])
    comments_for_answers = data_manager.get_comments_for_answers(list_with_answer_id)
    applied_tags = data_manager.get_tags_for_question(question_id)
    comments_q_len = len(comments_to_questions) + 2
    print(comments_for_answers)
    return render_template('display_question_and_answers.html', question=question[0], answers=answers,
                           applied_tags=applied_tags,
                           comments_to_questions=comments_to_questions, comments_for_answers=comments_for_answers,
                           comments_q_len=comments_q_len)


# load add question page
@app.route("/add-question", methods=['GET', 'POST'])
def add_question():
    if request.method == 'GET':
        return render_template('add-question.html')
    title = request.form.get('title')
    question = request.form.get('question')
    image = request.files['image']
    question_id = data_manager.add_question_to_file(title, question, image)
    return redirect('/question/' + str(question_id))


# add new answer to question
@app.route("/question/<question_id>/new-answer", methods=['GET', 'POST'])
def add_answer(question_id):
    if request.method == 'POST':
        message = request.form['new_answer']
        image = request.files['image']
        data_manager.add_answer_to_file(question_id, message, image)
        return redirect('/question/' + str(question_id))
    title = connection.get_title_by_id(question_id)
    return render_template('add_new_answer.html', question_id=question_id, title=title)


@app.route("/question/<question_id>/new-comment", methods=['GET', 'POST'])
def add_comment_to_question(question_id):
    if request.method == 'POST':
        message = request.form['new_comment']
        data_manager.add_comment_to_question(question_id, message)
        return redirect('/question/' + str(question_id))
    title = connection.get_title_by_id(question_id)
    return render_template('add_comment_to_question.html', question_id=question_id, title=title)


@app.route("/answer/<answer_id>/new-comment", methods=['GET', 'POST'])
def add_comment_to_answer(answer_id):
    if request.method == 'POST':
        message = request.form['new_comment']
        data_manager.add_comment_to_answer(answer_id, message)
        question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
        return redirect('/question/' + str(question_id))
    return render_template('add_comment_to_answer.html', answer_id=answer_id)


# delete question
@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    images_to_delete = [connection.get_from_db('image', 'question', 'id', question_id)]
    answers_id = connection.get_answer_id_connected_to_question(question_id)
    for id in answers_id:
        images_to_delete.append(connection.get_from_db('image', 'answer', 'id', id))
        connection.delete_from_db('comment', 'answer_id', id)
    for image in images_to_delete:
        if os.path.isfile(f"static/uploads/{image}"):
            os.remove(f"static/uploads/{image}")
    connection.delete_from_db('comment', 'question_id', question_id)
    connection.delete_from_db('question_tag', 'question_id', question_id)
    connection.delete_from_db('answer', 'question_id', question_id)
    connection.delete_from_db('question', 'id', question_id)
    return redirect('/list')


# edit question
@app.route("/question/<question_id>/edit", methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        question_to_edit = connection.get_question_to_edit(question_id)
        return render_template('edit-question.html', question_to_edit=question_to_edit)
    edited_title = request.form.get('title')
    edited_question = request.form.get('question')
    connection.update_question(question_id, edited_title, edited_question)
    return redirect('/list')


# edit answer
@app.route("/answer/<answer_id>/edit", methods=['GET', 'POST'])
def edit_answer(answer_id):
    if request.method == 'GET':
        answer_to_edit = connection.get_answer_to_edit(answer_id)
        return render_template('edit-answer.html', answer_to_edit=answer_to_edit)
    edited_answer = request.form.get('answer')
    connection.update_answer(answer_id, edited_answer)
    return redirect('/list')


# edit comment
@app.route("/comment/<comment_id>/edit", methods=['GET', 'POST'])
def edit_comment(comment_id):
    if request.method == 'GET':
        comment_to_edit = connection.get_comment_to_edit(comment_id)
        return render_template('edit-comment.html', comment_to_edit=comment_to_edit)
    edited_comment = request.form.get('comment')
    connection.update_comment(comment_id, edited_comment)
    connection.change_value_db('comment', 'edited_count', '+', 'id', comment_id)
    question_id = connection.get_from_db("question_id", "comment", "id", comment_id)
    if not question_id:
        answer_id = connection.get_from_db("answer_id", "comment", "id", comment_id)
        question_id = connection.get_from_db("question_id", "answer", "id", answer_id)
    return redirect('/question/' + str(question_id))


# delete answer
@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    image_to_delete = connection.get_from_db('image', 'answer', 'id', answer_id)
    if os.path.isfile(f"static/uploads/{image_to_delete}"):
        os.remove(f"static/uploads/{image_to_delete}")
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    connection.delete_from_db('answer', 'id', answer_id)
    connection.delete_from_db('comment', 'answer_id', answer_id)
    return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_up")
def vote_up_question(question_id):
    connection.change_value_db('question', 'vote_number', '+', 'id', question_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_down")
def vote_down_question(question_id):
    connection.change_value_db('question', 'vote_number', '-', 'id', question_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_up")
def vote_up_answer(answer_id):
    connection.change_value_db('answer', 'vote_number', '+', 'id', answer_id)
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_down")
def vote_down_answer(answer_id):
    connection.change_value_db('answer', 'vote_number', '-', 'id', answer_id)
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


@app.route("/show_image/<image>/<question_id>")
def show_image(image, question_id):
    return render_template('show_image.html', image=image, question_id=question_id)


@app.route("/question/<question_id>/new-tag", methods=['GET'])
def add_new_tag(question_id):
    tags = connection.get_all_existing_tags()
    applied_tags = data_manager.get_tags_for_question(question_id)
    return render_template('add-tag.html', tags=tags, question_id=question_id, applied_tags=applied_tags)


@app.route("/question/<question_id>/new-tag", methods=['POST'])
def handle_new_tag(question_id):
    new_defined_tags = request.form.get('new-tags')
    data_manager.add_new_defined_tags(new_defined_tags, question_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/new-tag/<tag>")
def add_tags_to_question(question_id, tag):
    tag_id = connection.get_id_by_tag(tag)
    connection.apply_tag_to_question(question_id, tag_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/new-tag/<tag>/delete")
def delete_tags_from_question(question_id, tag):
    tag_id = connection.get_id_by_tag(tag)
    connection.delete_tag_from_question(question_id, tag_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/<tag>/delete")
def delete_tags_from_question2(question_id, tag):
    tag_id = connection.get_id_by_tag(tag)
    connection.delete_tag_from_question(question_id, tag_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


# delete comment
@app.route("/comments/<comment_id>/delete")
def delete_comment(comment_id):
    question_id = connection.get_from_db("question_id", "comment", "id", comment_id)
    if not question_id:
        answer_id = connection.get_from_db("answer_id", "comment", "id", comment_id)
        question_id = connection.get_from_db("question_id", "answer", "id", answer_id)
    connection.delete_from_db('comment', 'id', comment_id)
    return redirect('/question/' + str(question_id))


if __name__ == "__main__":
    app.run()
