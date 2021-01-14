CREATE TYPE PokemonType AS ENUM (
	'Bug',
    'Fire',
    'Normal',
    'Dark',
    'Flying',
    'Poison',
    'Dragon',
    'Ghost',
    'Psychic',
    'Electric',
    'Grass',
    'Rock',
    'Fairy',
    'Ground',
    'Steel',
    'Fighting',
    'Ice',
    'Water'
);

CREATE TABLE IF NOT EXISTS "Pokemon"(
    id, uuid PRIMARY KEY,
    name, varchar(255) NOT NULL,
    number, integer NOT NULL,
    main_type, pokemontype NOT NULL,
    secondary_type, pokemontype,
    hp, integer NOT NULL,
    atk, integer NOT NULL,
    def, integer NOT NULL,
    spe_atk, integer NOT NULL,
    spe_def, integer NOT NULL,
    speed, integer NOT NULL,
    generation, integer NOT NULL,
    legendary, boolean NOT NULL
);

CREATE TABLE IF NOT EXISTS "User"(
    id uuid PRIMARY KEY,
    username varchar(20) NOT NULL UNIQUE,
    firebase_id varchar(255) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS "Favorite"(
    id uuid PRIMARY KEY,
    user_id uuid REFERENCES "User"(id),
    pokemon_id uuid REFERENCES "Pokemon"(id)
);


CREATE TABLE IF NOT EXISTS "Team"(
    id uuid PRIMARY KEY,
    name varchar(255) NOT NULL,
    user_id uuid REFERENCES "User"(id)
);


CREATE TABLE "PokemonTeam" (
    id uuid PRIMARY KEY,
    pokemon_id uuid REFERENCES "Pokemon"(id),
    team_id uuid REFERENCES "Team"(id)
);



