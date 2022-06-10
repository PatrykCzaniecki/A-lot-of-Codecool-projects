from flask import Flask, render_template, redirect, jsonify
from data import queries
from dotenv import load_dotenv
from util import json_response

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows')
def shows_redirect():
    return redirect('/shows/most_rated/1/rating/desc')


@app.route('/shows/most_rated')
def top_shows_redirect():
    return redirect('/shows/most_rated/1/rating/desc')


@app.route('/shows/most_rated/<current_page>/<order_by>/<order_as>')
def most_rated(current_page, order_by, order_as):
    if order_as == 'asc':
        order_as_opposite = 'desc'
        marker = '⇧'
    else:
        order_as_opposite = 'asc'
        marker = '⇩'
    asc_marker = '⇩'
    page_size = 15
    current_page = int(current_page)
    number_of_pages = queries.get_count()[0]['count'] // page_size
    page_data = (current_page - 1) * page_size
    top_shows = queries.get_top_shows(page_data, page_size, order_by, order_as)
    return render_template('most_rated.html', shows=top_shows, number_of_pages=number_of_pages,
                           current_page=current_page, order_by=order_by, order_as=order_as,
                           order_as_opposite=order_as_opposite, marker=marker, asc_marker=asc_marker)


@app.route('/show/<id>')
def show_page(id):
    show_info = queries.get_show_info(id)
    number_of_actors = len(show_info)
    video_id = show_info[0]['trailer'][27:]
    hour = 0
    while show_info[0]['runtime'] >= 60:
        show_info[0]['runtime'] -= 60
        hour += 1
    minute = show_info[0]['runtime']
    if hour != 0 and minute != 0:
        runtime = f'{hour}h {minute}min'
    elif hour != 0 and minute == 0:
        runtime = f'{hour}h'
    else:
        runtime = f'{minute}min'
    season_info = queries.get_season_info(id)
    return render_template('show_page.html', show_info=show_info, actorlist=number_of_actors, video_id=video_id,
                           runtime=runtime, season_info=season_info)


@app.route('/api/task/<year_from>/<year_to>')
@json_response
def task_api(year_from, year_to):
    year_from = str(year_from) + '-01-01'
    year_to = str(year_to) + '-12-31'
    actors = queries.get_actors_for_task(year_from, year_to)
    return actors


@app.route('/task')
def task():
    return render_template('task.html')


@app.route('/penguins')
def penguins():
    return render_template('penguins.html')


@app.route('/api/penguins/<season_number>')
@json_response
def penguins_api(season_number):
    season_number = int(season_number)
    list_of_episodes = queries.get_episodes_for_season(season_number)
    return list_of_episodes


@app.route('/movie')
def movie():
    return render_template('movie.html')


@app.route('/api/movie/<title>')
@json_response
def movie_api(title):
    title = str(title)
    show_id = queries.get_id_of_movie(title)
    show_id = show_id[0]['id']

    list_of_actors_id = queries.get_actors_id_for_movie(show_id)

    actors = []
    for actor in list_of_actors_id:
        actors.append(actor['actor_id'])

    list_of_actors = queries.get_actors_for_movie(actors)
    return list_of_actors


@app.route('/house')
def characters_list_for_house():
    characters_list = queries.get_characters()
    return render_template('house.html', characters=characters_list)


@app.route('/actor/<actor_id>')
@json_response
def main_actor_details(actor_id):
    actor_details = queries.get_actor_details(actor_id)
    actor_details['birthday'] = str(actor_details['birthday'])
    return actor_details


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
