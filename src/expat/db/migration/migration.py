from expat.db.migration.models import Migration

from pathlib import Path


def get_migrations(migration_dir: Path) -> list[Migration]:
    migrations: list[Migration] = []

    for dir in sorted(migration_dir.iterdir()):
        if not dir.is_dir():
            continue

        migration = Migration.from_path(dir)

        migrations.append(migration)
    
    return migrations


