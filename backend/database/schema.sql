PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS character_quests;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS quests;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS difficulties;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS rarities;
DROP TABLE IF EXISTS item_types;
DROP TABLE IF EXISTS alignments;
DROP TABLE IF EXISTS species;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE
        CHECK (length(email) <= 255),
    display_name TEXT NOT NULL UNIQUE
        CHECK (length(display_name) <= 100),
    password_hash TEXT NOT NULL,
    date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL UNIQUE
        CHECK (length(class_name) <= 50),
    description TEXT
);

CREATE TABLE species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_name TEXT NOT NULL UNIQUE
        CHECK (length(species_name) <= 50),
    description TEXT
);

CREATE TABLE alignments (
    alignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    alignment_name TEXT NOT NULL UNIQUE
        CHECK (length(alignment_name) <= 50),
    description TEXT
);

CREATE TABLE item_types (
    item_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE
        CHECK (length(type_name) <= 50),
    description TEXT
);

CREATE TABLE rarities (
    rarity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rarity_name TEXT NOT NULL UNIQUE
        CHECK (length(rarity_name) <= 50),
    description TEXT
);

CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name TEXT NOT NULL UNIQUE
        CHECK (length(region_name) <= 100),
    description TEXT
);

CREATE TABLE difficulties (
    difficulty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    difficulty_name TEXT NOT NULL UNIQUE
        CHECK (length(difficulty_name) <= 50),
    description TEXT
);

CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    character_name TEXT NOT NULL CHECK (length(character_name) <= 100),
    character_type TEXT NOT NULL CHECK (character_type IN ('Player', 'NPC')),
    class_id INTEGER NOT NULL,
    species_id INTEGER NOT NULL,
    alignment_id INTEGER NOT NULL,
    level INTEGER NOT NULL DEFAULT 1 CHECK (level >= 1),

    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id),
    FOREIGN KEY (alignment_id) REFERENCES alignments(alignment_id)
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL UNIQUE,
    description TEXT,
    item_type_id INTEGER NOT NULL,
    rarity_id INTEGER NOT NULL,

    FOREIGN KEY (item_type_id) REFERENCES item_types(item_type_id),
    FOREIGN KEY (rarity_id) REFERENCES rarities(rarity_id)
);

CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity >= 1),

    UNIQUE (character_id, item_id)

    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE quests (
    quest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    quest_name TEXT NOT NULL UNIQUE
        CHECK (length(quest_name) <= 100),
    region_id INTEGER NOT NULL,
    difficulty_id INTEGER NOT NULL,

    FOREIGN KEY (region_id) REFERENCES regions(region_id),
    FOREIGN KEY (difficulty_id) REFERENCES difficulties(difficulty_id)
);

CREATE TABLE character_quests (
    character_quest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id INTEGER NOT NULL,
    quest_id INTEGER NOT NULL,
    completion_date DATETIME,

    FOREIGN KEY (character_id) REFERENCES characters(character_id),
    FOREIGN KEY (quest_id) REFERENCES quests(quest_id),

    UNIQUE (character_id, quest_id)
);