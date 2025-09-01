from expat.config import ExpatConfig

from pathlib import Path
from pytest import fixture


@fixture
def test_config():
    return ExpatConfig(
        migration_dir=Path(__file__).parent.parent / "test_data" / "migrations"
    )
