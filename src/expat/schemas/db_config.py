from expat.expat_types import ExpandableString
from expat.schemas.base import Base

from pydantic import SecretStr, field_serializer

from typing import Any, Literal, final


DBType = Literal["mysql", "postgresql"]


class DBConfig(Base):
    type: DBType


@final
class PostgreSQLConfig(DBConfig):
    type: DBType = "postgresql"

    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: SecretStr = SecretStr("postgres")
    database_name: str = "postgres"
    schema_name: str = "expat"

    connection_options: dict[str, str] = {}

    @field_serializer("password", when_used="json")
    def dump_password(self, password: SecretStr) -> str:
        return password.get_secret_value()


@final
class MySQLConfig(DBConfig):
    type: DBType = "mysql"

    host: ExpandableString = "localhost"
    port: int = 3306
    user: str = "root"
    password: SecretStr = SecretStr("mysql")
    schema_name: str = "expat"

    connection_options: dict[str, Any] = {}

    @field_serializer("password", when_used="json")
    def dump_password(self, password: SecretStr) -> str:
        return password.get_secret_value()
