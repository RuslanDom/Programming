DROP TABLE IF EXISTS movie_direction;
DROP TABLE IF EXISTS movie_cast;


CREATE TABLE IF NOT EXISTS director(
    dir_id INTEGER PRIMARY KEY,
    dir_first_name VARCHAR(50),
    dir_last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS movie(
    mov_id INTEGER PRIMARY KEY,
    mov_title VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS actors(
    act_id INTEGER PRIMARY KEY,
    act_first_name VARCHAR(50),
    act_last_name VARCHAR(50),
    gender VARCHAR(1)
);

CREATE TABLE IF NOT EXISTS movie_direction(
    dir_id INTEGER,
    mov_id INTEGER,
    FOREIGN KEY(dir_id) REFERENCES director(dir_id) ON DELETE CASCADE,
    FOREIGN KEY(mov_id) REFERENCES movie(mov_id) ON DELETE CASCADE
--     PRIMARY KEY(dir_id, mov_id)
);

CREATE TABLE IF NOT EXISTS oscar_awarded(
    award_id INTEGER PRIMARY KEY,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS movie_cast(
    act_id INTEGER REFERENCES actors(act_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE,
    role VARCHAR(50)
--     PRIMARY KEY(act_id, mov_id)
);