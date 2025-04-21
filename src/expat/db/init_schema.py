from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed.dbapi import DBAPIConnection

from expat.types import Flavour

import pathlib


def schema_up(connection: DBAPIConnection, flavour: Flavour) -> None:
    schema_dir = get_schema_dir(flavour)
    up_file = schema_dir / "up.sql"

    with open(up_file, "r") as f:
        script = f.read()

    cursor = connection.cursor()
    cursor.execute(script)
    cursor.close()


def schema_down(connection: DBAPIConnection, flavour: Flavour) -> None:
    schema_dir = get_schema_dir(flavour)
    down_file = schema_dir / "down.sql"

    with open(down_file, "r") as f:
        script = f.read()

    cursor = connection.cursor()
    cursor.execute(script)
    cursor.close()


def get_schema_dir(flavour: Flavour) -> pathlib.Path:
    init_schema_dir = pathlib.Path(__file__).parent.parent.parent.parent / "init_schema"

    match flavour:
        case "sqlite":
            return init_schema_dir / "sqlite"
        case _:
            raise ValueError(f"Invalid SQL flavour: {flavour}")

