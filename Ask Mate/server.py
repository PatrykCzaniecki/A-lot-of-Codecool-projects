import os
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
import connection
import data_manager


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "grgrewhre"
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
    alert = data_manager.is_logged(session)
    if 'user_id' in session:
        user_id = session['user_id']
    else:
        user_id = False
    if searched_phrase:
        all_searched_questions, searched_answers = connection.search_in_questions_and_answers(searched_phrase)
        all_searched_questions = connection.mark_searched_phrase(all_searched_questions, searched_phrase)
        if len(searched_answers) > 0:
            searched_answers = connection.mark_searched_phrase_in_answers(searched_answers, searched_phrase)
        return render_template('search.html',
                               searched_phrase=searched_phrase, data=all_searched_questions, headers=headers,
                               searched_answers=searched_answers, alert=alert)
    return render_template('index.html', data=data_five_questions, headers=headers, alert=alert, user_id=user_id)


# load question list page
@app.route("/list")
def list_questions():
    alert = data_manager.is_logged(session)
    headers, data_questions = data_manager.list_prepare_question_to_show()
    order = request.args.get('order_by')
    direction = request.args.get('order_direction')
    if order or direction:
        data_questions = connection.sort_questions(order, direction)
    return render_template('list.html', data=data_questions, headers=headers, alert=alert)


# load question detail page
@app.route('/question/<question_id>')
def question_display(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    user_id = session['user_id']
    connection.change_value_db('question', 'view_number', '+', 'id', question_id)
    question, answers, comments_to_questions = data_manager.question_display_by_id_with_answers(question_id)
    list_with_answer_id = []
    for answer in answers:
        list_with_answer_id.append(answer['id'])
    comments_for_answers = data_manager.get_comments_for_answers(list_with_answer_id)
    applied_tags = data_manager.get_tags_for_question(question_id)
    comments_q_len = len(comments_to_questions) + 2
    return render_template('display_question_and_answers.html', question=question[0], answers=answers,
                           applied_tags=applied_tags,
                           comments_to_questions=comments_to_questions, comments_for_answers=comments_for_answers,
                           comments_q_len=comments_q_len, alert=alert, user_id=user_id)


# load add question page
@app.route("/add-question", methods=['GET', 'POST'])
def add_question():
    if request.method == 'GET':
        alert = data_manager.is_logged(session)
        if alert is True:
            return redirect('/login')
        return render_template('add-question.html', alert=alert)
    title = request.form.get('title')
    question = request.form.get('question')
    image = request.files['image']
    user_id = session['user_id']
    question_id = data_manager.add_question_to_file(title, question, image, user_id)
    return redirect('/question/' + str(question_id))


# add new answer to question
@app.route("/question/<question_id>/new-answer", methods=['GET', 'POST'])
def add_answer(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    if request.method == 'POST':
        message = request.form['new_answer']
        image = request.files['image']
        user_id = session['user_id']
        data_manager.add_answer_to_file(question_id, message, image, user_id)
        return redirect('/question/' + str(question_id))
    title = connection.get_title_by_id(question_id)
    return render_template('add_new_answer.html', question_id=question_id, title=title, alert=alert)


@app.route("/question/<question_id>/new-comment", methods=['GET', 'POST'])
def add_comment_to_question(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    if request.method == 'POST':
        message = request.form['new_comment']
        user_id = session['user_id']
        data_manager.add_comment_to_question(question_id, message, user_id)
        return redirect('/question/' + str(question_id))
    title = connection.get_title_by_id(question_id)
    return render_template('add_comment_to_question.html', question_id=question_id, title=title, alert=alert)


@app.route("/answer/<answer_id>/new-comment", methods=['GET', 'POST'])
def add_comment_to_answer(answer_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    if request.method == 'POST':
        user_id = session['user_id']
        message = request.form['new_comment']
        data_manager.add_comment_to_answer(answer_id, message, user_id)
        question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
        title = connection.get_title_by_id(question_id)
        return redirect('/question/' + str(question_id))
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    title = connection.get_title_by_id(question_id)
    return render_template('add_comment_to_answer.html', answer_id=answer_id, alert=alert, title=title,
                           question_id=question_id)


# delete question
@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    user_id = session['user_id']
    creator_id = connection.get_user_id_by_other_id(question_id, 'question')
    if creator_id == user_id:
        images_to_delete = [connection.get_from_db('image', 'question', 'id', question_id)]
        answers_id = connection.get_answer_id_connected_to_question(question_id)
        for id in answers_id:
            images_to_delete.append(connection.get_from_db('image', 'answer', 'id', id))
            connection.delete_from_db('comment', 'answer_id', id)
        for image in images_to_delete:
            if os.path.isfile(f"static/uploads/{image}"):
                os.remove(f"static/uploads/{image}")
        data_manager.delete_by_id(question_id)
        return redirect('/list')
    return redirect('/question/' + str(question_id))


# edit question
@app.route("/question/<question_id>/edit", methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'GET':
        alert = data_manager.is_logged(session)
        if alert is True:
            return redirect('/login')
        user_id = session['user_id']
        creator_id = connection.get_user_id_by_other_id(question_id, 'question')
        if user_id == creator_id:
            question_to_edit = connection.get_question_to_edit(question_id)
            return render_template('edit-question.html', question_to_edit=question_to_edit, alert=alert,
                                   question_id=question_id)
        else:
            return redirect('/question/' + str(question_id))
    edited_title = request.form.get('title')
    edited_question = request.form.get('question')
    connection.update_question(question_id, edited_title, edited_question)
    return redirect('/question/' + str(question_id))


# edit answer
@app.route("/answer/<answer_id>/edit", methods=['GET', 'POST'])
def edit_answer(answer_id):

    if request.method == 'GET':
        alert = data_manager.is_logged(session)
        if alert is True:
            return redirect('/login')
        user_id = session['user_id']
        creator_id = connection.get_user_id_by_other_id(answer_id, 'answer')
        if user_id == creator_id:
            answer_to_edit = connection.get_answer_to_edit(answer_id)
            question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
            return render_template('edit-answer.html', answer_to_edit=answer_to_edit, alert=alert,
                                   question_id=question_id)
        else:
            return redirect('/answer/' + str(answer_id))
    edited_answer = request.form.get('answer')
    connection.update_answer(answer_id, edited_answer)
    return redirect('/list')


# edit comment
@app.route("/comment/<comment_id>/edit", methods=['GET', 'POST'])
def edit_comment(comment_id):
    if request.method == 'GET':
        alert = data_manager.is_logged(session)
        if alert is True:
            return redirect('/login')
        user_id = session['user_id']
        creator_id = connection.get_user_id_by_other_id(comment_id, 'comment')
        if user_id == creator_id:
            comment_to_edit = connection.get_comment_to_edit(comment_id)
            question_id = connection.get_from_db("question_id", "comment", "id", comment_id)
            if not question_id:
                answer_id = connection.get_from_db("answer_id", "comment", "id", comment_id)
                question_id = connection.get_from_db("question_id", "answer", "id", answer_id)
            return render_template('edit-comment.html', comment_to_edit=comment_to_edit, alert=alert,
                                   question_id=question_id)
        else:
            return redirect('/comment/' + str(comment_id))
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
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    user_id = session['user_id']
    creator_id = connection.get_user_id_by_other_id(answer_id, 'answer')
    if user_id == creator_id:
        image_to_delete = connection.get_from_db('image', 'answer', 'id', answer_id)
        if os.path.isfile(f"static/uploads/{image_to_delete}"):
            os.remove(f"static/uploads/{image_to_delete}")
        question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
        connection.delete_from_db('comment', 'answer_id', answer_id)
        connection.delete_from_db('answer', 'id', answer_id)
        return redirect('/question/' + str(question_id))
    else:
        question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
        return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_up")
def vote_up_question(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    creator_id = connection.get_user_id_by_other_id(question_id, 'question')
    connection.change_value_db('question', 'vote_number', '+', 'id', question_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    connection.change_reputation('+', '5', creator_id)
    return redirect('/question/' + str(question_id))


@app.route("/question/<question_id>/vote_down")
def vote_down_question(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    creator_id = connection.get_user_id_by_other_id(question_id, 'question')
    connection.change_value_db('question', 'vote_number', '-', 'id', question_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    connection.change_reputation('-', '2', creator_id)
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_up")
def vote_up_answer(answer_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    creator_id = connection.get_user_id_by_other_id(answer_id, 'answer')
    connection.change_value_db('answer', 'vote_number', '+', 'id', answer_id)
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    connection.change_reputation('+', '10', creator_id)
    return redirect('/question/' + str(question_id))


@app.route("/answer/<answer_id>/vote_down")
def vote_down_answer(answer_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    creator_id = connection.get_user_id_by_other_id(answer_id, 'answer')
    connection.change_value_db('answer', 'vote_number', '-', 'id', answer_id)
    question_id = connection.get_from_db('question_id', 'answer', 'id', answer_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    connection.change_reputation('-', '2', creator_id)
    return redirect('/question/' + str(question_id))


@app.route("/show_image/<image>/<question_id>")
def show_image(image, question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    return render_template('show_image.html', image=image, question_id=question_id, alert=alert)


@app.route("/question/<question_id>/new-tag", methods=['GET'])
def add_new_tag(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    tags = connection.get_all_existing_tags()
    applied_tags = data_manager.get_tags_for_question(question_id)
    return render_template('add-tag.html', tags=tags, question_id=question_id, applied_tags=applied_tags, alert=alert)


@app.route("/question/<question_id>/new-tag", methods=['POST'])
def handle_new_tag(question_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    new_defined_tags = request.form.get('new-tags')
    data_manager.add_new_defined_tags(new_defined_tags, question_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/new-tag/<tag>")
def add_tags_to_question(question_id, tag):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    tag_id = connection.get_id_by_tag(tag)
    connection.apply_tag_to_question(question_id, tag_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/new-tag/<tag>/delete")
def delete_tags_from_question(question_id, tag):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    tag_id = connection.get_id_by_tag(tag)
    connection.delete_tag_from_question(question_id, tag_id)
    return redirect('/question/' + str(question_id) + '/new-tag')


@app.route("/question/<question_id>/<tag>/delete")
def delete_tags_from_question2(question_id, tag):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    tag_id = connection.get_id_by_tag(tag)
    connection.delete_tag_from_question(question_id, tag_id)
    connection.change_value_db('question', 'view_number', '-', 'id', question_id)
    return redirect('/question/' + str(question_id))


# delete comment
@app.route("/comments/<comment_id>/delete")
def delete_comment(comment_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    question_id = connection.get_from_db("question_id", "comment", "id", comment_id)
    if not question_id:
        answer_id = connection.get_from_db("answer_id", "comment", "id", comment_id)
        question_id = connection.get_from_db("question_id", "answer", "id", answer_id)
    connection.delete_from_db('comment', 'id', comment_id)
    return redirect('/question/' + str(question_id))


# registration endpoint
@app.route("/registration", methods=['GET', 'POST'])
def registration():
    alert = data_manager.is_logged(session)
    if alert is False:
        return redirect('/')
    if request.method == 'GET':
        return render_template('registration.html', alert=alert)
    username = request.form['username']
    password = request.form['password']
    is_username_taken = data_manager.user_registration(username, password)
    if not is_username_taken:
        return redirect('/')
    else:
        return render_template('registration.html', error='Username already exists', alert=alert)


@app.route("/users")
def display_all_users():
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/')
    headers, users_data = data_manager.list_prepare_users_to_show()
    return render_template('list_of_users.html', headers=headers, data=users_data, alert=alert)


# user profile page
@app.route("/user/<user_id>")
def user_profile_page(user_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    user_data, user_questions, user_answers, user_comments = data_manager.user_profile_page(user_id)
    return render_template('profile_page.html', data=user_data, questions=user_questions, answers=user_answers,
                           comments=user_comments, alert=alert)


# user login function
@app.route("/login", methods=['GET', 'POST'])
def login():
    alert = data_manager.is_logged(session)
    if alert is False:
        return redirect('/')
    if request.method == 'GET':
        return render_template('login.html', alert=alert)
    username = request.form['username']
    plain_text_password = request.form['password']
    if connection.username_exists(username):
        hashed_password = connection.get_password(username)
        if data_manager.verify_password(plain_text_password, hashed_password):
            session['username'] = username
            session['user_id'] = connection.get_user_id_by_name(username)
            return redirect('/')
    error_message = 'Invalid username or password'
    return render_template('login.html', error_message=error_message, alert=alert)


# logout from user account
@app.route('/logout')
def logout():
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect('/')


# accepting answers
@app.route('/<question_id>/<answer_id>/accept_answer')
def accept_answer(question_id, answer_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    answer_owner = connection.get_user_id_by_other_id(answer_id, 'answer')
    creator_id = connection.get_user_id_by_other_id(question_id, 'question')
    if creator_id != session['user_id']:
        return redirect('/question/' + str(question_id))
    if session['user_id'] == answer_owner:
        return redirect('/question/' + str(question_id))
    connection.accept_answer(answer_id)
    answer_owner = connection.get_user_id_by_other_id(answer_id, 'answer')
    connection.change_reputation('+', '15', answer_owner)
    return redirect('/question/' + str(question_id))


# not accepting answers
@app.route('/<question_id>/<answer_id>/not_accept_answer')
def not_accept_answer(question_id, answer_id):
    alert = data_manager.is_logged(session)
    if alert is True:
        return redirect('/login')
    creator_id = connection.get_user_id_by_other_id(question_id, 'question')
    answer_owner = connection.get_user_id_by_other_id(answer_id, 'answer')
    if creator_id != session['user_id']:
        return redirect('/question/' + str(question_id))
    if session['user_id'] == answer_owner:
        return redirect('/question/' + str(question_id))
    connection.dont_accept_answer(answer_id)
    connection.change_reputation('-', '15', answer_owner)
    return redirect('/question/' + str(question_id))


@app.route('/tags')
def display_all_tags():
    alert = data_manager.is_logged(session)
    headers, users_data = data_manager.list_prepare_tags_to_show()
    return render_template('display-tags.html', headers=headers, data=users_data, alert=alert)


if __name__ == "__main__":
    app.run()
