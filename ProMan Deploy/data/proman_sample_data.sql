--
-- PostgreSQL database Proman
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

SET default_with_oids = false;

---
--- drop tables
---

DROP TABLE IF EXISTS statuses CASCADE;
DROP TABLE IF EXISTS boards CASCADE;
DROP TABLE IF EXISTS cards;

---
--- create tables
---

CREATE TABLE statuses (
    id       SERIAL PRIMARY KEY     NOT NULL,
    title    VARCHAR(200)           NOT NULL
);

CREATE TABLE boards (
    id          SERIAL PRIMARY KEY  NOT NULL,
    title       VARCHAR(200)        NOT NULL
);

CREATE TABLE cards (
    id          SERIAL PRIMARY KEY  NOT NULL,
    board_id    INTEGER             NOT NULL,
    status_id   INTEGER             NOT NULL,
    title       VARCHAR (200)       NOT NULL,
    card_order  INTEGER             NOT NULL,
    archive     VARCHAR (10)        default 'false'
);
CREATE TABLE IF NOT EXISTS users (
    id       SERIAL PRIMARY KEY     NOT NULL,
    name     VARCHAR(200)           NOT NULL,
    password VARCHAR(200)        NOT NULL
);

---
--- insert data
---




---
--- add constraints
---

ALTER TABLE ONLY cards
    ADD CONSTRAINT fk_cards_board_id FOREIGN KEY (board_id) REFERENCES boards(id);

ALTER TABLE ONLY cards
    ADD CONSTRAINT fk_cards_status_id FOREIGN KEY (status_id) REFERENCES statuses(id);

alter table boards
    add private int default 0 not null;

alter table boards
    add user_id int default Null;

alter table boards
    add constraint boards_users_id_fk
        foreign key (user_id) references users;

alter table statuses
    add board_id int;

alter table statuses
    add constraint statuses_boards_id_fk
        foreign key (board_id) references boards;

INSERT INTO statuses(title,board_id) VALUES ('new',1);
INSERT INTO statuses(title,board_id) VALUES ('in progress',1);
INSERT INTO statuses(title,board_id) VALUES ('testing',2);
INSERT INTO statuses(title,board_id) VALUES ('done',2);

INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 1, 'new card 1', 1, 'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 1, 'new card 2', 2, 'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 1, 'new card 3', 4, 'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 1, 'new card 4', 3, 'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 2, 'in progress card', 1,'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 3, 'planning', 1,'true');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 4, 'done card 1', 1,'true');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 1, 4, 'done card 1', 2,'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 1, 'new card 1', 1,'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 1, 'new card 2', 2,'true');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 2, 'in progress card', 1,'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 3, 'planning', 1,'false');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 4, 'done card 1', 1,'true');
INSERT INTO cards VALUES (nextval('cards_id_seq'), 2, 4, 'done card 1', 2,'false');



