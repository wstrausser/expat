from expat.db import init_schema

import pytest

import pathlib
import sqlite3


@pytest.fixture
def sqlite_db():
    db_path = pathlib.Path("test.db")
    connection = sqlite3.connect(db_path)
    
    yield connection

    connection.close()
    db_path.unlink()


def test_schema_up_sqlite(sqlite_db: sqlite3.Connection):
    init_schema.init_schema(sqlite_db)
