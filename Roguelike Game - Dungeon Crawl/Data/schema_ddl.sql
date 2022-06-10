DROP TABLE IF EXISTS dbo.game_state;
CREATE TABLE dbo.game_state (
    id int IDENTITY (1,1) PRIMARY KEY,
    current_map varchar(max) NOT NULL,
    saved_at datetime2 DEFAULT GETDATE() NOT NULL,
    player_id integer NOT NULL
);
DROP TABLE IF EXISTS dbo.player;
CREATE TABLE dbo.player (
    id int IDENTITY (1,1) PRIMARY KEY,
    player_name varchar(max) NOT NULL,
    hp integer NOT NULL,
	damage integer NOT NULL,
	shield integer NOT NULL,
    x integer NOT NULL,
    y integer NOT NULL,
	map integer NOT NULL
);

DROP TABLE IF EXISTS dbo.inventory;
CREATE TABLE dbo.inventory (
    id int IDENTITY (1,1) PRIMARY KEY,
    item_name varchar(20) NOT NULL,
    amount integer NOT NULL
);
ALTER TABLE dbo.game_state
    ADD CONSTRAINT fk_player_id FOREIGN KEY (player_id) REFERENCES dbo.player(id);