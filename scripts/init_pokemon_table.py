import csv
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from uuid import uuid4

import psycopg2

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = Path(FILE_DIR) / ".."


DATABASE_URL = "postgres://pokedex:pokedex@127.0.0.1:5432/poke"
parsed_dabatase_url = urlparse(DATABASE_URL)
db_username = parsed_dabatase_url.username
db_password = parsed_dabatase_url.password
db_hostname = parsed_dabatase_url.hostname
database = parsed_dabatase_url.path[1:]

conn: Any = None

try:
    conn = psycopg2.connect(
        database=database,
        user=db_username,
        password=db_password,
        host=db_hostname,
    )
except Exception as e:
    print(e)
    print("Unable to connect to the database")

cursor = conn.cursor()

insert_request = """
    INSERT INTO "Pokemon"(
        id,
        name,
        number,
        main_type,
        secondary_type,
        hp,
        atk,
        def,
        spe_atk,
        spe_def,
        speed,
        generation,
        legendary
    ) VALUES
"""

with open(PROJECT_DIR / "data" / "pokemon.csv") as pokemon_csv:
    reader = csv.DictReader(pokemon_csv, delimiter=",")
    values_to_insert = []

    for row in reader:
        type_2_interpolation = (
            f"'{row['Type 2']}'" if len(row["Type 2"]) > 0 else "NULL"
        )

        values_to_insert.append(
            f"('{str(uuid4())}',"
            f"'{row['Name']}',"
            f"{row['#']},"
            f"'{row['Type 1']}',"
            f"{type_2_interpolation},"
            f"{row['HP']},"
            f"{row['Attack']},"
            f"{row['Defense']},"
            f"{row['Sp. Atk']},"
            f"{row['Sp. Def']},"
            f"{row['Speed']},"
            f"{row['Generation']},"
            f"{row['Legendary'].lower()})"
        )

    values_str = f"{','.join(values_to_insert)};"
    insert_request = insert_request + values_str
    pokemon_csv.close()

try:
    cursor.execute(insert_request)
    conn.commit()
    print("All Pokemons are in the database")
except Exception as e:
    print(e)
    print("Cannot execute SQL Insert")
finally:
    cursor.close()
    conn.close()
