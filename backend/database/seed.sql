PRAGMA foreign_keys = ON;

INSERT INTO players (email, display_name, password_hash) VALUES
('aurora@example.com', 'AuroraPrime', '$2b$12$K8sdf8sdf8sdf8sdf8sdfu8sdf'),
('kylie@example.com', 'Kaylie_xo', '$2b$12$9xsd9f8sdf7sdf8sdf8sdf7sdf'),
('dockrat@example.com', 'DockRatBob', '$2b$12$asd89f7sdf98sdf7sdf98sdf7');

INSERT INTO classes (class_name, description) VALUES
('Plasma Knight', 'A frontline fighter using energy blades.'),
('Void Ranger', 'A ranged specialist trained for deep-space survival.'),
('Star Pilot', 'A tactical pilot skilled in navigation and combat.');

INSERT INTO species (species_name) VALUES
('Human'),
('Synth'),
('Lunari');

INSERT INTO alignments (alignment_name) VALUES
('Lawful Good'),
('Neutral'),
('Chaotic Neutral');

INSERT INTO item_types (type_name) VALUES
('Weapon'),
('Armour'),
('Potion');

INSERT INTO rarities (rarity_name) VALUES
('Common'),
('Rare'),
('Legendary');

INSERT INTO regions (region_name) VALUES
('Orion Belt'),
('Nebula Wastes'),
('Titan Outpost');

INSERT INTO difficulties (difficulty_name) VALUES
('Easy'),
('Medium'),
('Hard');

INSERT INTO characters (
    player_id,
    character_name,
    character_type,
    class_id,
    species_id,
    alignment_id,
    level
) VALUES
(1, 'AuroraPrime', 'Player', 1, 1, 1, 12),
(1, 'Aurora_Alt', 'Player', 2, 2, 2, 4),
(2, 'DockRatBob', 'Player', 3, 1, 3, 9),
(3, 'Nebula Warden', 'NPC', 1, 3, 2, 15);

INSERT INTO items (
    item_name,
    item_type_id,
    rarity_id
) VALUES
('Photon Blade', 1, 3),
('Void Shield', 2, 2),
('Med Gel', 3, 1),
('Star Map Fragment', 1, 2);

INSERT INTO inventory (
    character_id,
    item_id,
    quantity
) VALUES
(1, 1, 1),
(1, 3, 5),
(2, 2, 1),
(3, 4, 2);

INSERT INTO quests (
    quest_name,
    region_id,
    difficulty_id
) VALUES
('Recover the Lost Signal', 1, 1),
('Defend Titan Outpost', 3, 2),
('Escape the Nebula Wastes', 2, 3);

INSERT INTO character_quests (
    character_id,
    quest_id,
    completion_date
) VALUES
(1, 1, '2026-02-01 14:30:00'),
(2, 2, NULL),
(3, 3, '2026-02-03 19:45:00');