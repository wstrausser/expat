from expat.schemas.toml.migration_toml import MigrationToml


def test_migration_toml_dump(default_migration_toml: MigrationToml, default_migration_toml_dumped: str):
    actual = default_migration_toml.model_dump_toml()
    expected = default_migration_toml_dumped

    assert actual == expected


def test_migration_toml_load(default_migration_toml: MigrationToml, default_migration_toml_dumped: str):
    actual = default_migration_toml
    expected = MigrationToml.model_load_toml(default_migration_toml_dumped)

    assert actual == expected
