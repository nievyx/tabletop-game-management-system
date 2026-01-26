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

CREATE TABLE profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    display_name TEXT NOT NULL, -- Displays names not unique, can be shared accross muliple accounts
    created_at DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL UNIQUE, 
    description TEXT
);

CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    profile_id INTEGER NOT NULL, 
    class_id INTEGER NOT NULL, 
    level INTEGER NOT NUll DEFAULT 1 CHECK (level >= 1), -- Characters start at level 1 (Fail Safe)
    FOREIGN KEY (profile_id) REFERENCES profiles(profile_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id) 
);

CREATE TABLE quests (
    quest_id, 
    title, 
    difficulty
);

CREATE TABLE character_quests (
    character_id, 
    quest_id, 
    status, 
    started_at, 
    completed_at
);

CREATE TABLE asset_types (
    asset_type_id, 
    name
);

CREATE TABLE assets (
    asset_id, 
    title,
    asset_type_id
);

CREATE TABLE licenses (
    license_id, 
    user_id, 
    asset_id, 
    status, 
    issued_at, 
    expires_at
);
