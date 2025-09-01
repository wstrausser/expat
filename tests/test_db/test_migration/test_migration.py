from expat.config import ExpatConfig
from expat.db.migration import get_migrations
from expat.db.migration import Migration, MigrationRow

import sqlite3


def test_get_migrations(test_config: ExpatConfig):
    migrations = get_migrations(test_config.migration_dir)

    assert migrations == [
        Migration(
            migration_path=test_config.migration_dir / "20250901113604839_test-migration-1",
            migration_id="20250901113604839",
            migration_name="test-migration-1",
            up_hash="d41d8cd98f00b204e9800998ecf8427e",
            down_hash="d41d8cd98f00b204e9800998ecf8427e",
        ),
        Migration(
            migration_path=test_config.migration_dir / "20250901114236057_test-migration-2",
            migration_id="20250901114236057",
            migration_name="test-migration-2",
            up_hash="d41d8cd98f00b204e9800998ecf8427e",
            down_hash="d41d8cd98f00b204e9800998ecf8427e",
        )
    ]


def test_migration_insert(test_migrations: list[Migration], initialized_sqlite_db: sqlite3.Connection):
    migration = test_migrations[0]

    migration._insert(initialized_sqlite_db)

    cursor = initialized_sqlite_db.cursor()
    cursor.execute("SELECT * FROM migrations;")
    result = cursor.fetchall()
    cursor.close()

    migrations = [MigrationRow.from_row(row) for row in result]

    assert migrations == [
        MigrationRow(
            migration_id="20250901113604839",
            migration_name="test-migration-1",
            up_hash="d41d8cd98f00b204e9800998ecf8427e",
            down_hash="d41d8cd98f00b204e9800998ecf8427e",
        )
    ]


def test_migration_is_applied(test_migrations: list[Migration], initialized_sqlite_db: sqlite3.Connection):
    migration = test_migrations[0]

    migration._insert(initialized_sqlite_db)

    is_applied = migration._is_applied(initialized_sqlite_db)

    assert is_applied
