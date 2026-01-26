CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE auth_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    event_time DATETIME NOT NULL,
    ip_hash TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE profiles ()

CREATE TABLE classes ()

CREATE TABLE characters ()

CREATE TABLE quests ()

CREATE TABLE character_quests ()

CREATE TABLE asset_types ()

CREATE TABLE assets ()

CREATE TABLE licenses ()
