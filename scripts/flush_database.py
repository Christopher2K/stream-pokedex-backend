# flake8: noqa
from typing import Any
from urllib.parse import urlparse

import psycopg2

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

try:
    cursor.execute(
        "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name"  # noqa
    )
    rows = cursor.fetchall()

    for row in rows:
        print("dropping table: ", row[1])
        cursor.execute('DROP TABLE IF EXISTS "' + row[1] + '" CASCADE;')
        conn.commit()

    cursor.execute(
        """
        SELECT      n.nspname as schema, t.typname as type
        FROM        pg_type t
        LEFT JOIN   pg_catalog.pg_namespace n ON n.oid = t.typnamespace
        WHERE       (t.typrelid = 0 OR (SELECT c.relkind = 'c' FROM pg_catalog.pg_class c WHERE c.oid = t.typrelid))
        AND     NOT EXISTS(SELECT 1 FROM pg_catalog.pg_type el WHERE el.oid = t.typelem AND el.typarray = t.oid)
        AND     n.nspname NOT IN ('pg_catalog', 'information_schema');
    """
    )

    rows = cursor.fetchall()

    for row in rows:
        print("dropping type: ", row[1])
        cursor.execute('DROP TYPE IF EXISTS "' + row[1] + '";')
        conn.commit()

    cursor.close()
    conn.close()
except Exception as e:
    print(e)
    print("Error while trying to delete all tables")
