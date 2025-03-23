from expat.schemas.toml.meta_toml import MetaToml

from datetime import UTC, datetime
from importlib.metadata import version
import textwrap


def test_meta_toml_dump(default_meta_toml: MetaToml):
    created_time = default_meta_toml.created_time

    expected_date = (
        f"{created_time.year}-{created_time.month:02d}-{created_time.day:02d}T"
        f"{created_time.hour:02d}:{created_time.minute:02d}:{created_time.second:02d}."
        f"{created_time.microsecond:06d}Z"
    )

    actual = default_meta_toml.model_dump_toml()
    expected = f"""\
        created_time = "{expected_date}"
        id = "{default_meta_toml.id}"
        expat_version = "{version("expat")}"
    """

    assert actual == textwrap.dedent(expected)


def test_meta_toml_load():
    actual = MetaToml.model_load_toml(
        f"""
            created_time = "1900-01-01T00:00:00.000000Z"
            id = "7e6a3394933a2ba1da4fbb75ce066ea4"
            expat_version = "{version("expat")}"
        """
    )

    expected = MetaToml(
        created_time=datetime(1900, 1, 1, 0, 0, 0, 0, UTC),
        id="7e6a3394933a2ba1da4fbb75ce066ea4",
        expat_version=version("expat"),
    )

    assert actual == expected
