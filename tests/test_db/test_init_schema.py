from expat.db import init_schema

import sqlite3


def test_schema_up_sqlite(sqlite_db: sqlite3.Connection):
    init_schema.init_schema(sqlite_db)
