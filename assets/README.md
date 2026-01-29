

[![Database Sample Data Demo](CAPTURE.PNG)](https://niamhdev.com)

Diagram created @ https://dbdiagram.io/

<details>
<summary> </summary>

```
Table users {
  user_id int [pk, increment]
  email text [not null, unique]
  password_hash text [not null]
  created_at date [not null]
}

Table auth_events {
  event_id int [pk, increment]
  user_id int [not null]
  event_type text [not null]
  event_time datetime [not null]
  ip_hash text [not null]
}

Table profiles {
  profile_id int [pk, increment]
  user_id int [not null]
  display_name text [not null]
  created_at date [not null]
}

Table classes {
  class_id int [pk, increment]
  name text [not null, unique]
  description text
}

Table characters {
  character_id int [pk, increment]
  profile_id int [not null]
  class_id int [not null]
  level int [not null]
}

Table quests {
  quest_id int [pk, increment]
  title text [not null, unique]
  difficulty text [not null]
}

Table character_quests {
  character_id int [not null]
  quest_id int [not null]
  status text [not null]
  started_at date [not null]
  completed_at date

  indexes {
    (character_id, quest_id) [pk]
  }
}

Table asset_types {
  asset_type_id int [pk, increment]
  name text [not null, unique]
}

Table assets {
  asset_id int [pk, increment]
  title text [not null, unique]
  asset_type_id int [not null]
}

Table licenses {
  license_id int [pk, increment]
  user_id int [not null]
  asset_id int [not null]
  status text [not null]
  issued_at date [not null]
  expires_at date

  indexes {
    (user_id, asset_id) [unique]
  }
}

Ref: auth_events.user_id > users.user_id
Ref: profiles.user_id > users.user_id
Ref: characters.profile_id > profiles.profile_id
Ref: characters.class_id > classes.class_id
Ref: character_quests.character_id > characters.character_id
Ref: character_quests.quest_id > quests.quest_id
Ref: assets.asset_type_id > asset_types.asset_type_id
Ref: licenses.user_id > users.user_id
Ref: licenses.asset_id > assets.asset_id
```


</details>
