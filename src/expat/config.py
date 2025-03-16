from pydantic import BeforeValidator, Field, SecretStr, model_validator
from pydantic_settings import BaseSettings

import logging
import os
import tomllib
from typing import Annotated, Any, Literal, Self, Type


logger = logging.getLogger(__name__)


ExpandableString = Annotated[str, BeforeValidator(lambda s: os.path.expandvars(s))]
LogLevel = Literal["critical", "error", "warning", "info", "debug"]
DBType = Literal["postgres", "mysql"]


class Config(BaseSettings, case_sensitive=True, populate_by_name=True):
    config_file: ExpandableString | None = Field(alias="EXPAT_CONFIG_FILE")

    db_type: DBType = Field(alias="EXPAT_DB_TYPE")
    db_host: str = Field(alias="EXPAT_DB_HOST")
    db_port: int = Field(alias="EXPAT_DB_PORT")
    db_database: str | None = Field(alias="EXPAT_DB_DATABASE", default=None)
    db_user: str = Field(alias="EXPAT_DB_USER")
    db_password: SecretStr = Field(alias="EXPAT_DB_PASSWORD")
    db_options: dict[str, Any] = Field(alias="EXPAT_DB_OPTIONS", default={})

    log_level: LogLevel = Field(alias="EXPAT_LOG_LEVEL")

    @classmethod
    def from_file(cls: Type[Self], config_path: str) -> Self:
        config_dict = {}

        config_dict["EXPAT_CONFIG_FILE"] = config_path

        with open(config_path, "rb") as f:
            config_toml = tomllib.load(f)

        tables = ["database", "logs"]

        for table_name in tables:
            table = config_toml[table_name]
            for key, value in table.items():
                config_dict[key] = value

        return cls(**config_dict)

    @property
    def python_log_level(self) -> str:
        return self.log_level.upper()

    @model_validator(mode="after")
    def check_database_field(self) -> Self:
        if self.db_type == "mysql" and self.db_database is not None:
            raise ValueError("'db_database' setting should not be used with mysql")
        elif self.db_type == "postgres" and self.db_database is None:
            raise ValueError("'db_database' must be set with postgres")

        return self

    def show(self) -> None:
        log_string = ""
        for key, value in self.model_dump().items():
            log_string += f"\n        {key.ljust(20, ' ')} = {value}"

        logger.info(f"Configuration loaded successfully:{log_string}\n")
