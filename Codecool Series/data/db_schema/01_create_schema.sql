DROP TABLE IF EXISTS show_genres;
DROP TABLE IF EXISTS show_characters;
DROP TABLE IF EXISTS episodes;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS shows;


CREATE TABLE shows (
    id       INTEGER PRIMARY KEY NOT NULL,
    title    VARCHAR(200)        NOT NULL,
    year     DATE                NULL,
    overview TEXT,
    runtime  SMALLINT,
    trailer  VARCHAR(200),
    homepage VARCHAR(200),
    rating   NUMERIC
);


CREATE TABLE genres (
    id   SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30)        NOT NULL
);


CREATE TABLE actors (
    id        INTEGER PRIMARY KEY NOT NULL,
    name      VARCHAR(200)        NOT NULL,
    birthday  DATE,
    death     DATE,
    biography TEXT
);


CREATE TABLE seasons (
    id            INTEGER PRIMARY KEY NOT NULL,
    season_number SMALLINT            NOT NULL,
    title         VARCHAR(200),
    overview      TEXT,
    show_id       INTEGER             NOT NULL
);


CREATE TABLE show_genres (
    id       SERIAL PRIMARY KEY NOT NULL,
    show_id  INTEGER            NOT NULL,
    genre_id INTEGER            NOT NULL
);


CREATE TABLE show_characters (
    id             SERIAL PRIMARY KEY NOT NULL,
    show_id        INTEGER            NOT NULL,
    actor_id       INTEGER            NOT NULL,
    character_name VARCHAR(200)       NOT NULL
);


CREATE TABLE episodes (
    id             INTEGER PRIMARY KEY NOT NULL,
    title          VARCHAR(200),
    episode_number SMALLINT            NOT NULL,
    overview       TEXT,
    season_id      INTEGER             NOT NULL
);


ALTER TABLE ONLY seasons
    ADD CONSTRAINT fk_seasons_show_id FOREIGN KEY (show_id) REFERENCES shows(id);


ALTER TABLE ONLY episodes
    ADD CONSTRAINT fk_episodes_season_id FOREIGN KEY (season_id) REFERENCES seasons(id);


ALTER TABLE ONLY show_characters
    ADD CONSTRAINT fk_show_characters_actor_id FOREIGN KEY (actor_id) REFERENCES actors(id);


ALTER TABLE ONLY show_characters
    ADD CONSTRAINT fk_show_characters_show_id FOREIGN KEY (show_id) REFERENCES shows(id);


ALTER TABLE ONLY show_genres
    ADD CONSTRAINT fk_show_genres_genre_id FOREIGN KEY (genre_id) REFERENCES genres(id);

ALTER TABLE ONLY show_genres
    ADD CONSTRAINT fk_show_genres_show_id FOREIGN KEY (show_id) REFERENCES shows(id);
