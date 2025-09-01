from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed.dbapi import DBAPIConnection

import pathlib


def schema_up(connection: DBAPIConnection) -> None:
    schema_dir = get_schema_dir()
    up_file = schema_dir / "up.sql"

    with open(up_file, "r") as f:
        script = f.read()

    cursor = connection.cursor()
    cursor.execute(script)
    cursor.close()


def schema_down(connection: DBAPIConnection) -> None:
    schema_dir = get_schema_dir()
    down_file = schema_dir / "down.sql"

    with open(down_file, "r") as f:
        script = f.read()

    cursor = connection.cursor()
    cursor.execute(script)
    cursor.close()


def get_schema_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent.parent.parent / "init_schema"
