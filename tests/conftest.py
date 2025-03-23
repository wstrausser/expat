from expat.schemas.db_config import MySQLConfig, PostgreSQLConfig
from expat.schemas.toml.expat_toml import ExpatConfig, ExpatToml
from expat.schemas.toml.meta_toml import MetaToml
from expat.schemas.toml.migration_toml import MigrationToml, MigrationConfig

import pytest


@pytest.fixture()
def default_expat_config() -> ExpatConfig:
    return ExpatConfig()


@pytest.fixture
def default_postgres_config() -> PostgreSQLConfig:
    return PostgreSQLConfig()


@pytest.fixture
def default_mysql_config() -> MySQLConfig:
    return MySQLConfig()


@pytest.fixture
def default_expat_toml_postgres(
    default_expat_config: ExpatConfig, default_postgres_config: PostgreSQLConfig
) -> ExpatToml[PostgreSQLConfig]:
    return ExpatToml(expat=default_expat_config, database=default_postgres_config)


@pytest.fixture
def default_expat_toml_mysql(
    default_expat_config: ExpatConfig, default_mysql_config: MySQLConfig
) -> ExpatToml[MySQLConfig]:
    return ExpatToml(expat=default_expat_config, database=default_mysql_config)


@pytest.fixture
def default_meta_toml() -> MetaToml:
    return MetaToml()


@pytest.fixture
def default_migration_toml() -> MigrationToml:
    return MigrationToml(
        migration=MigrationConfig(
            label="test_label",
            comment="Test comment",
        ),
    )
