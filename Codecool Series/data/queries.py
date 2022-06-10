from data import data_manager
from psycopg2._psycopg import AsIs


def get_shows():
    query = '''
        SELECT id, title 
        FROM shows;'''

    return data_manager.execute_select(query)


def get_top_shows(page_data, page_size, order_by, order_as):
    query = '''
        SELECT shows.id, title, to_char(year, 'YYYY') as year, runtime, round(rating, 1) as rating, 
        STRING_AGG(genres.name,', ') as genres, trailer, homepage      
        FROM shows
        left join show_genres on shows.id = show_genres.show_id
        left join genres on show_genres.genre_id = genres.id
        GROUP BY shows.id, title, year, runtime, rating, trailer, homepage
        ORDER BY %(order_by)s %(order_as)s
        LIMIT %(page_size)s
        OFFSET %(page_data)s;'''

    return data_manager.execute_select(query, {'page_data': page_data, 'page_size': page_size,
                                               'order_by': AsIs(order_by), 'order_as': AsIs(order_as)})


def get_count():
    query = '''
        SELECT count(id)
        FROM shows;'''

    return data_manager.execute_select(query)


def get_show_info(id):
    query = '''
        SELECT shows.id, title, trailer, runtime, round(rating, 1) as rating,
        string_agg(genres.name, ', ' order by genres.name) as genres,
        coalesce(trailer, 'no_url') as trailer, year, actors.name as actors 
        FROM shows
        left join show_genres on shows.id = show_genres.show_id
        left join genres on show_genres.genre_id = genres.id
        left join show_characters on shows.id = show_characters.show_id
        left join actors on show_characters.actor_id = actors.id
        WHERE shows.id = %(id)s
        GROUP BY title, runtime, rating, trailer, year, shows.id, actors;'''

    return data_manager.execute_select(query, {'id': id})


def get_season_info(id):
    query = '''
        SELECT seasons.title, seasons.overview, season_number 
        FROM seasons
        left join shows on seasons.show_id = shows.id
        WHERE shows.id = %(id)s
        ORDER BY season_number;'''

    return data_manager.execute_select(query, {'id': id})


def get_actors_for_task(year_from, year_to):
    query = '''
        SELECT name, to_char(birthday, 'YYYY') as birthday
        FROM actors
        WHERE birthday BETWEEN %(year_from)s AND %(year_to)s
        ORDER BY name DESC;'''

    return data_manager.execute_select(query, {'year_from': year_from, 'year_to': year_to})


def get_penguins_id():
    query = '''
        SELECT id, title
        FROM shows
        WHERE shows.title LIKE ('The Penguins of Madagascar')'''

    return data_manager.execute_select(query)


def get_season_id():
    query = '''
        SELECT id
        FROM seasons
        where show_id = 7823;'''

    return data_manager.execute_select(query)


def get_episodes_for_season(season_number):
    query = '''
        SELECT title, overview
        FROM episodes
        WHERE season_id = %(season_number)s;'''

    return data_manager.execute_select(query, {'season_number': season_number})


def get_id_of_movie(title):
    query = '''
        SELECT id
        FROM shows
        WHERE title = %(title)s'''

    return data_manager.execute_select(query, {'title': title})


def get_actors_id_for_movie(show_id):
    query = '''
        SELECT actor_id
        FROM show_characters
        WHERE show_id = %(show_id)s'''

    return data_manager.execute_select(query, {'show_id': show_id})


def get_actors_for_movie(actors):
    actors_name = []

    for actor in actors:
        query = '''
            SELECT name, biography
            FROM actors
            WHERE id = %s'''
        actor_name = data_manager.execute_select(query, (actor, ))
        actors_name.append(actor_name)

    return actors_name


def get_characters():
    show_id = data_manager.execute_select(
        """
        SELECT id 
        FROM shows 
        WHERE title LIKE '%House%'""")[0]['id']
    return data_manager.execute_select(
        """
        SELECT actor_id, character_name 
        FROM show_characters 
        WHERE show_id = (%s)""", (show_id,))


def get_actor_details(actor_id):
    return data_manager.execute_select(
        """
        SELECT name, birthday 
        FROM actors 
        WHERE id = (%s)""", (actor_id,))[0]
