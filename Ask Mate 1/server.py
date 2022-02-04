from flask import Flask, render_template, request, redirect
import connection
import os
from werkzeug.utils import secure_filename
import data_manager


QUESTION_TITLE = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
ANSWER_TITLE = ["id", "submission_time", "vote_number", "question_id", "message", "image"]
QUESTION_DATABASE_LENGTH = len(QUESTION_TITLE)
ANSWER_DATABASE_LENGTH = len(ANSWER_TITLE)

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


# path for answer database
def answer_path():
    return 'sample_data/answer.csv'


# path for question database
def question_path():
    return 'sample_data/question.csv'


# load home page
@app.route("/")
def home_page():
    return redirect('/list')


# load question list page
@app.route("/list")
def list_questions():
    headers, data_questions = data_manager.list_prepare_question_to_show()
    if request.method == 'GET':
        order = request.args.get('order_by')
        direction = request.args.get('order_direction')
        data_manager.list_sort_question(data_questions, order, direction)
    return render_template('list.html', data=data_questions, headers=headers)


# load question detail page
@app.route('/question/<question_id>')
def question_display(question_id):
    question, answers = data_manager.question_display_by_id_with_answers(question_id)
    return render_template('display_question_and_answers.html', question=question, answers=answers)


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


# delete question
@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    connection.delete_from_file(question_id, question_path(), answer_path())
    return redirect('/list')


# edit question
@app.route("/question/<question_id>/edit", methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        question_to_edit = connection.get_question_to_edit(question_id)
        return render_template('edit-question.html', question_to_edit=question_to_edit)
    edited_title = request.form.get('title')
    edited_question = request.form.get('question')
    data_manager.edit_question_pass_data_to_file(question_id, edited_title, edited_question)
    return redirect('/list')


# delete answer
@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    question_id = connection.delete_answer_from_file(answer_id, answer_path())
    return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_up")
def vote_up_question(question_id):
    connection.vote(question_path(), question_id, vote='+')
    return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_down")
def vote_down_question(question_id):
    connection.vote(question_path(), question_id, vote='-')
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_up")
def vote_up_answer(answer_id):
    question_id = connection.vote(answer_path(), answer_id, vote='+')
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_down")
def vote_down_answer(answer_id):
    question_id = connection.vote(answer_path(), answer_id, vote='-')
    return redirect('/question/' + str(question_id))


@app.route("/show_image/<image>/<question_id>")
def show_image(image, question_id):
    return render_template('show_image.html', image=image, question_id=question_id)


if __name__ == "__main__":
    app.run()
