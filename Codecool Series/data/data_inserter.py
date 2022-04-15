import datetime
import os
import sys

import requests
from psycopg2 import DataError

import init_db
from data_manager import execute_select, execute_dml_statement

from dotenv import load_dotenv

load_dotenv()

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': os.environ.get('TRAKT_API_KEY')
}
TRAKT_API_URL = 'https://api.trakt.tv'
TRAKT_MAX_LIMIT = 20
TRAKT_MAX_SHOW_COUNT = 52500


def should_use_trakt():
    print("The program can try connecting to the TRAKT API to download data or use local data to insert instead (faster)?")
    answer = input("Do you want to connect to the TRAKT API? (y/n) ")
    return answer.lower() == "y"

def main():
    # We don't have documentation for trakt, so students shouldn't be exposed to it
    # if you want to re-enable it by adding documentation about trakt to the project
    # README then use should_use_trakt() instead of False
    use_trakt = False
    # init_db.init_db()
    # init_db.create_schema()
    if use_trakt:
        insert_genres()
        insert_shows(limit=20, max_show_count=100)
        print('Data downloaded and inserted successfully')
    else:
        execute_sql_file("data/dump_1000_shows/codecool_public_genres.sql")
        print("Genres inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_shows.sql")
        print("Shows inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_show_genres.sql")
        print("Show genres inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_seasons.sql")
        print("Seasons inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_episodes.sql")
        print("Episodes inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_actors.sql")
        print("Actors inserted")
        execute_sql_file("data/dump_1000_shows/codecool_public_show_characters.sql")
        print("Show characters inserted")

    print("Your database should work now!")


def execute_sql_file(filename):
    with open(filename, encoding="utf8") as file:
        execute_dml_statement(file.read())


def insert_genres():
    url = f'{TRAKT_API_URL}/genres/movies'
    genre_request = requests.get(url, headers=headers)
    counter = 0
    trakt_expected_genre_count = len(genre_request.json())

    for i, genre in enumerate(genre_request.json()):
        statement = "INSERT INTO genres (name) VALUES (%(name)s);"
        execute_dml_statement(statement, {'name': genre['name']})

        progress_bar(i, trakt_expected_genre_count, prefix='Inserting genres:')
        counter = i
    clear_progress_bar('Inserted ' + str(counter) + ' genres')


def insert_shows(limit=20, max_show_count=1000):
    limit = max(1, min(limit, TRAKT_MAX_LIMIT))
    max_show_count = max(1, min(max_show_count, TRAKT_MAX_SHOW_COUNT))

    inserted_ids = []
    result_page = 1
    total_counter = 0
    while total_counter < max_show_count:
        url = f"{TRAKT_API_URL}/shows/popular?limit={limit}&page={result_page}&extended=full"
        result_page += 1
        result_set = requests.get(url, headers=headers)
        if result_set == '[]':
            break

        for show_raw in result_set.json():
            # If max_show_count is not dividable by the limit, we have to jump out before processing all received shows
            if total_counter >= max_show_count:
                break

            show = get_show_entity(show_raw)

            # Some shorts have no id, some has no date, etc... Skip these
            if show['id'] is None or show['year'] is None:
                continue

            statement = """
                INSERT INTO shows (id, title, year, overview, runtime, trailer, homepage, rating)
                VALUES (%(id)s, %(title)s, %(year)s, %(overview)s, %(runtime)s, %(trailer)s, %(homepage)s, %(rating)s);"""

            try:
                execute_dml_statement(statement, show)
                inserted_ids.append(show['id'])

                if len(show['genres']) > 0:
                    genre_ids = get_genre_ids(show['genres'])
                    insert_genres_of_show(genre_ids, show)

            except DataError:
                print('Error while inserting ' + show['title'] + '. Skipping this show...')
            # except IntegrityError:
            #    print('Show (' + show['title'] + ') already exists...')

            insert_seasons_of_show(show['id'])
            insert_cast_of_show(show['id'])

            progress_bar(total_counter + 1, max_show_count, prefix='Inserting shows:', suffix=show['title'])
            total_counter += 1

    clear_progress_bar('Inserted ' + str(len(inserted_ids)) + ' shows')
    return inserted_ids


def insert_seasons_of_show(show_id):
    url = f'{TRAKT_API_URL}/shows/{str(show_id)}/seasons?extended=full,episodes'
    season_request = requests.get(url, headers=headers)
    for season_raw in season_request.json():
        statement = """
            INSERT INTO seasons ( id, season_number, title, overview, show_id)
            VALUES (%(id)s, %(season_number)s, %(title)s, %(overview)s, %(show_id)s);
        """

        season = get_season_entity(season_raw, show_id)
        execute_dml_statement(statement, season)

        insert_episodes_of_season(season)


def insert_cast_of_show(show_id):
    url = "{api_url}/shows/{show_id}/people?extended=full".format(
        api_url=TRAKT_API_URL,
        show_id=show_id
    )

    result_set = requests.get(url, headers=headers).json()

    if 'cast' in result_set:
        for actor in result_set['cast']:
            insert_actor_of_show(show_id, actor)


def insert_genres_of_show(genre_ids, show_entity):
    for genre_id in genre_ids:
        execute_dml_statement("""
            INSERT INTO show_genres (show_id, genre_id)
            VALUES (%(show_id)s, %(genre_id)s); """, {
            'show_id': show_entity['id'],
            'genre_id': genre_id
        })


def insert_actor_of_show(show_id, actor):
    actor_id = actor['person']['ids']['trakt']
    existing_actor = execute_select("SELECT id FROM actors WHERE id=%(actor_id)s", {'actor_id': actor_id})

    if len(existing_actor) == 0:
        execute_dml_statement("""
            INSERT INTO actors (id, name, birthday, death, biography)
            VALUES (%(id)s, %(name)s, %(birthday)s, %(death)s, %(biography)s);
        """, {
            "id": actor_id,
            "name": actor['person']['name'],
            "birthday": actor['person']['birthday'],
            "death": actor['person']['death'],
            "biography": actor['person']['biography']
        })

    execute_dml_statement("""
        INSERT INTO show_characters (show_id, actor_id, character_name)
        VALUES (%(show_id)s, %(actor_id)s, %(character_name)s)
    """, {
        'show_id': show_id,
        'actor_id': actor_id,
        'character_name': actor['character']
    })


def insert_episodes_of_season(season):
    for episode in season['episodes']:
        stmt = """
            INSERT INTO episodes (
                id,
                title,
                episode_number,
                overview,
                season_id)
            VALUES (
                %(id)s,
                %(title)s,
                %(episode_number)s,
                %(overview)s,
                %(season_id)s
            );
        """
        execute_dml_statement(stmt, get_episode_entity(season['id'], episode))


def get_show_entity(show):
    show_entity = {
        'id': show['ids']['trakt'],
        'title': show['title'],
        'year': None,
        'overview': show['overview'],
        'runtime': show['runtime'],
        'trailer': show['trailer'],
        'homepage': show['homepage'],
        'genres': show['genres'],
        'rating': show['rating']
    }
    try:
        show_entity['year'] = datetime.date(show['year'], 1, 1)
    except TypeError:
        pass
    return show_entity


def get_season_entity(season, show_id):
    season_entity = {
        'id': season['ids']['trakt'],
        'season_number': season['number'],
        'title': season['title'],
        'overview': season['overview'],
        'episodes': [],
        'episode_count': season['episode_count'],
        'show_id': show_id
    }
    if 'episodes' in season:
        season_entity['episodes'] = season['episodes']

    return season_entity


def get_episode_entity(season_id, episode):
    return {
        'id': episode['ids']['trakt'],
        'title': episode['title'],
        'episode_number': episode['number'],
        'overview': episode['overview'],
        'season_id': season_id
    }


def get_genre_ids(genre_list):
    genres = tuple((g.title() for g in genre_list))
    id_result = execute_select("SELECT id FROM genres WHERE name IN %s;", (genres,))
    genre_ids = [result['id'] for result in id_result]
    return genre_ids


# original: https://stackoverflow.com/a/27871113/2205458
def progress_bar(count, total, prefix='', suffix=''):
    max_prefix_length = 18
    max_suffix_length = 18
    terminal_width = get_terminal_width()
    prefix = trim_string(prefix, max_prefix_length)
    suffix = trim_string(suffix, max_suffix_length, False)
    bar_length = terminal_width - 18 - max_prefix_length - max_suffix_length - (len(str(total)) * 2)
    filled_len = int(round(bar_length * count / float(total)))

    # changes shape in every 0.33 sec
    spinner = ['⋮', '⋯', '⋰', '⋱'][int(float(datetime.datetime.utcnow().strftime("%s.%f")) * 3) % 4]

    sys.stdout.write(
        ' {prefix} ▐{bar}▌ {percents: >5}% ({count: >{counter_length}}/{total}) {spinner} {suffix}\r'.format(
            prefix=prefix,
            bar='◼' * filled_len + '◻' * (bar_length - filled_len),
            percents=round(100.0 * count / float(total), 1),
            count=count,
            total=total,
            spinner=spinner,
            counter_length=len(str(total)),
            suffix=suffix
        ))
    sys.stdout.flush()


def get_terminal_width():
    try:
        return int(os.get_terminal_size(0)[0])
    except OSError:
        return 80


def trim_string(text, length, align_right=True):
    if len(text) > length:
        return '{0: <{length}}'.format(text[:(length - 2)] + '..', length=length)
    else:
        return text.rjust(length) if align_right else text.ljust(length)


def clear_progress_bar(text=''):
    print(text + ' ' * (get_terminal_width() - len(text)))


if __name__ == '__main__':
    main()
