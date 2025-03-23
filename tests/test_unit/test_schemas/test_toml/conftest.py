import pytest

import textwrap


@pytest.fixture
def default_expat_toml_postgres_dumped() -> str:
    text = """\
        [expat]
        mode = "dev"
        include_down_files = true
        enable_interactive_mode = true
        split_commands = true
        log_level = "NOTSET"

        [database.postgresql]
        host = "localhost"
        port = 5432
        user = "postgres"
        password = "postgres"
        database_name = "postgres"
        schema_name = "expat"
    """
    return textwrap.dedent(text)


@pytest.fixture
def default_expat_toml_mysql_dumped() -> str:
    text = """\
        [expat]
        mode = "dev"
        include_down_files = true
        enable_interactive_mode = true
        split_commands = true
        log_level = "NOTSET"

        [database.mysql]
        host = "localhost"
        port = 3306
        user = "root"
        password = "mysql"
        schema_name = "expat"
    """
    return textwrap.dedent(text)


@pytest.fixture
def default_migration_toml_dumped() -> str:
    text = """\
        [migration]
        label = "test_label"
        comment = "Test comment"
        apply_in_prod = true
        split_commands = true

        [migration.scripts]
        apply_scripts = ["./up.sql"]
        rollback_scripts = ["./down.sql"]
    """
    return textwrap.dedent(text)
