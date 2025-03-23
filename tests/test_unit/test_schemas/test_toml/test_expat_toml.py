from expat.schemas.db_config import MySQLConfig, PostgreSQLConfig
from expat.schemas.toml.expat_toml import ExpatToml


def test_expat_toml_dump_postgres(
    default_expat_toml_postgres: ExpatToml[PostgreSQLConfig], default_expat_toml_postgres_dumped: str
):
    actual = default_expat_toml_postgres.model_dump_toml()
    expected = default_expat_toml_postgres_dumped

    assert actual == expected


def test_expat_toml_dump_mysql(default_expat_toml_mysql: ExpatToml[MySQLConfig], default_expat_toml_mysql_dumped: str):
    actual = default_expat_toml_mysql.model_dump_toml()
    expected = default_expat_toml_mysql_dumped

    assert actual == expected


def test_expat_toml_load_postgres(
    default_expat_toml_postgres: ExpatToml[PostgreSQLConfig], default_expat_toml_postgres_dumped: str
):
    actual = ExpatToml.model_load_toml(default_expat_toml_postgres_dumped)
    expected = default_expat_toml_postgres

    assert actual == expected


def test_expat_toml_load_mysql(default_expat_toml_mysql: ExpatToml[MySQLConfig], default_expat_toml_mysql_dumped: str):
    actual = ExpatToml.model_load_toml(default_expat_toml_mysql_dumped)
    expected = default_expat_toml_mysql

    assert actual == expected
