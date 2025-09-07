from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed.dbapi import DBAPIConnection

from expat.config import ExpatConfig
from expat.db.init_schema import init_schema as _init_schema
from expat.db.migration import get_migrations as _get_migrations


def up(connection: DBAPIConnection, config: ExpatConfig) -> None:
    migrations = _get_migrations(config.migration_dir)

    _init_schema(connection)

    for migration in migrations:
        migration.apply(connection, config.validate_hashes)

def down(connection: DBAPIConnection, config: ExpatConfig) -> None:
    migrations = _get_migrations(config.migration_dir)
    migrations.reverse()

    for migration in migrations:
        migration.rollback(connection, config.validate_hashes)
