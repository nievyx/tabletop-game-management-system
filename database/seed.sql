PRAGMA foreign_keys = ON;

-- Users
INSERT INTO users(user_id, email, password_hash, created_at)
VALUES
(1, 'thea22hale@nove-system.com', 'HASHED_PASSWORD_1', '2025-01-01'),
(2, 'marloweroy101@nove-system.com', 'HASHED_PASSWORD_2', '2025-01-02'),
(3, 'kaylie-hull@nove-system.com', 'HASHED_PASSWORD_3', '2025-01-05');

-- Profiles
INSERT INTO profiles (profile_id, user_id, display_name, create_at)
VALUES
(1, 1, 'Daeryssa Strongreaver', '2025-01-01'), --Elf
(2, 1, 'Rubru Redblood', ' '2025-01-02'), --Goblin

--TODO: add more...

-- Races
INSERT INTO races (race_id, name, description)
VALUES
(1, 'Human', 'Adaptable and ambitious'),
(2, 'Elf', 'No description'),
(3, 'Goblin', 'No description'),
(4, 'Martian', 'No description');

-- Character Classes 
INVERT INTO classes (class_id, name, description)
VALUES
(1, 'Warrior', 'Frontline fighter with heavy armor'),
(2, 'Rogue', 'Stealth, crits, and gadgets'),
(3, 'Mage', 'Energy manipulation and battlefield control'),
(4, 'Cleric', 'Support, wards, and restoration'),
(5, 'Ranger', 'Tracking, ranged attacks, survival')

