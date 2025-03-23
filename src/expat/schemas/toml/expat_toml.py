from __future__ import annotations

from expat.schemas.base import Base, BaseToml
from expat.schemas.db_config import DBConfig, MySQLConfig, PostgreSQLConfig

from pydantic import TypeAdapter, model_validator

from typing import Any, Literal, final


@final
class ExpatToml[T: DBConfig](BaseToml):
    expat: ExpatConfig
    database: T

    @property
    def table_sort_order(self) -> list[str]:
        return ["expat", "database"]

    @model_validator(mode="before")
    def set_db_config(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        database = data["database"]

        if not isinstance(database, dict):
            return data

        db_keys = list(data["database"].keys())

        if len(db_keys) > 1:
            raise ValueError("Expat config file must only specify 1 database")

        db_type = db_keys[0]

        TypeAdapter(Literal["mysql", "postgresql"]).validate_python(db_type)

        match db_type:
            case "mysql":
                db_config = MySQLConfig(**data["database"]["mysql"], type=db_type)
            case "postgresql":
                db_config = PostgreSQLConfig(**data["database"]["postgresql"], type=db_type)
            case _:
                raise NotImplementedError

        data.update({"database": db_config})

        return data

    def toml_dump_hook(self, dumped: dict[Any, Any]) -> dict[Any, Any]:
        dumped["database"] = {self.database.type: self.database.model_dump(mode="json")}
        dumped["database"][self.database.type].pop("type")
        return dumped


@final
class ExpatConfig(Base):
    mode: Literal["prod", "dev"] = "dev"
    include_down_files: bool = True
    enable_interactive_mode: bool = True
    split_commands: bool = True
    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"] = "NOTSET"
