from expat.config import ExpatConfig
from expat.db.migration.migration import get_migrations
from expat.db.migration.models import Migration


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
