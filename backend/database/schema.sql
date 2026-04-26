PRAGMA foreign_keys = ON;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
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
    quest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE, 
    difficulty TEXT NOT NULL CHECK (difficulty IN ('Easy', 'Medium','Hard'))
    -- Difficulty levels stored as a constraint for simplicity.
    -- ( This could be refactored into lookup table if more difficulty setting introduced  )
);

CREATE TABLE character_quests (
    character_id INTEGER NOT NULL, 
    quest_id INTEGER NOT NULL, 
    status TEXT NOT NULL CHECK (status IN ('Completed', 'In Progress')),
    started_at DATE NOT NULL, 
    completed_at DATE, -- NULL when in progress
    PRIMARY KEY (character_id, quest_id),
    CHECK (
        (status = 'In Progress' AND completed_at IS NULL)
        OR
        (status = 'Completed' AND completed_at IS NOT NULL)
    ),
    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (quest_id) REFERENCES quests(quest_id)
);

CREATE TABLE asset_types (
    asset_type_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE assets (
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    asset_type_id INTEGER NOT NULL,
    FOREIGN KEY (asset_type_id) REFERENCES asset_types(asset_type_id)
);

CREATE TABLE licenses (
    license_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    asset_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('Active', 'Expired')),
    issued_at DATE NOT NULL,
    expires_at DATE,
    CHECK (
        (status = 'Active' AND expires_at IS NULL)
        OR
        (status = 'Expired' AND expires_at IS NOT NULL)
    ),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
    UNIQUE (user_id, asset_id) -- Prevents a user from having duplicate licenses

);
