PRAGMA foreign_keys = ON; -- Enable foreign key constraints at runtime

-- Users (hashed_password is a placeholder)
INSERT INTO users(user_id, email, password_hash, created_at)
VALUES
(1, 'thea22hale@nove-system.com', 'HASHED_PASSWORD_1', '2025-01-01'),
(2, 'marloweroy101@nove-system.com', 'HASHED_PASSWORD_2', '2025-01-02'),
(3, 'kaylie-hull@nove-system.com', 'HASHED_PASSWORD_3', '2025-01-05');

-- Auth Events (ip_hash is a placeholder)
INSERT INTO auth_events (event_id, user_id, event_type, event_time, ip_hash)
VALUES
(1, 1, 'LOGIN_SUCCESS', '2025-01-01 09:12:00', 'IP_HASH_A1'),
(2, 1, 'LOGIN_FAIL',    '2025-01-02 21:44:10', 'IP_HASH_A1'),
(3, 1, 'LOGIN_SUCCESS', '2025-01-02 21:46:02', 'IP_HASH_A1'),

(4, 2, 'LOGIN_FAIL',    '2025-01-03 08:20:11', 'IP_HASH_B7'),
(5, 2, 'LOGIN_FAIL',    '2025-01-03 08:21:05', 'IP_HASH_B7'),
(6, 2, 'LOGIN_SUCCESS', '2025-01-03 08:25:44', 'IP_HASH_B7'),

(7, 3, 'PASSWORD_RESET','2025-01-06 14:02:00', 'IP_HASH_C9'),
(8, 3, 'LOGIN_SUCCESS', '2025-01-06 14:06:30', 'IP_HASH_C9');


-- Profiles
INSERT INTO profiles (profile_id, user_id, display_name, created_at)
VALUES
(1, 1, 'AuroraPrime', '2025-01-01'),
(2, 1, 'Aurora_Alt',  '2025-01-06'),
(3, 2, 'DockRatBob',  '2025-01-02'),
(4, 3, 'SeraVoid',    '2025-01-05');


-- Character Classes 
INSERT INTO classes (class_id, name, description)
VALUES
(1, 'Void Ranger',   'Long-range scout with stealth tech and star-maps'),
(2, 'Plasma Knight', 'Frontline combatant wielding plasma blades and shields'),
(3, 'Synthmancer',   'Tech-sorcerer who bends drones, code, and circuitry'),
(4, 'Star Pilot',    'Ace flyer, evasive maneuvers, ship systems mastery');

-- Characters
INSERT INTO characters (character_id, profile_id, class_id, level)
VALUES
(1, 1, 2, 12),  -- AuroraPrime: Plasma Knight
(2, 2, 1, 4),   -- Aurora_Alt: Void Ranger
(3, 3, 4, 9),   -- DockRatBob: Star Pilot
(4, 4, 3, 15);  -- SeraVoid: Synthmancer

-- Quests / Tasks
INSERT INTO quests (quest_id, title, difficulty)
VALUES
(1, 'Ghost Signal at Kestrel Station',    'Medium'),
(2, 'Raid on the Helium Vaults of Ixion', 'Hard'),
(3, 'Escort the Pilgrim Barge "Eidolon"', 'Easy'),
(4, 'Purge the Nanite Cathedral',         'Hard'),
(5, 'Chart the Shatterbelt Nebula',       'Medium');

-- Character <-> Quests (Bridge Table)
INSERT INTO character_quests (character_id, quest_id, status, started_at, completed_at)
VALUES
(1, 1, 'Completed',   '2025-01-03', '2025-01-04'),
(1, 2, 'In Progress', '2025-01-08', NULL),
(2, 5, 'In Progress', '2025-01-10', NULL),
(3, 3, 'Completed',   '2025-01-04', '2025-01-04'),
(4, 4, 'Completed',   '2025-01-06', '2025-01-07');

-- Asset Types (DRM)
INSERT INTO asset_types (asset_type_id, name)
VALUES
(1, 'Expansion'),
(2, 'Soundtrack'),
(3, 'Cosmetic Pack'),
(4, 'Lore Compendium');

-- Assets
INSERT INTO assets (asset_id, title, asset_type_id)
VALUES
(1, 'Shatterbelt Nebula Expansion',     1),
(2, 'Songs of the Starforge (OST)',     2),
(3, 'Plasma Knight Armor Skins',        3),
(4, 'Codex: Factions of the Outer Rim', 4),
(5, 'Synthmancer Drone Familiar Pack',  3);

-- Licenses
INSERT INTO licenses (license_id, user_id, asset_id, status, issued_at, expires_at)
VALUES
(1, 1, 1, 'Active',  '2025-01-01', NULL),
(2, 1, 3, 'Active',  '2025-01-02', NULL),
(3, 2, 2, 'Expired', '2024-01-01', '2025-01-01'),
(4, 2, 4, 'Active',  '2025-01-02', NULL),
(5, 3, 5, 'Active',  '2025-01-05', NULL);

