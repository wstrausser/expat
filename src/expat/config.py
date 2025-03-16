from pydantic import BeforeValidator, Field, SecretStr
from pydantic_settings import BaseSettings

import logging
import os
import tomllib
from typing import Annotated, Literal, Self, Type


logger = logging.getLogger(__name__)


ExpandableString = Annotated[str, BeforeValidator(lambda s: os.path.expandvars(s))]
LogLevel = Literal["critical", "error", "warning", "info", "debug"]
DBType = Literal["postgres"]


class Config(BaseSettings, case_sensitive=True):
    config_file: ExpandableString | None = Field(alias="EXPAT_CONFIG_FILE")

    db_type: DBType = Field(alias="EXPAT_DB_TYPE")
    db_host: str = Field(alias="EXPAT_DB_HOST")
    db_port: int = Field(alias="EXPAT_DB_PORT")
    db_database: str = Field(alias="EXPAT_DB_DATABASE")
    db_user: str = Field(alias="EXPAT_DB_USER")
    db_password: SecretStr = Field(alias="EXPAT_DB_PASSWORD")
    db_options: dict[str, str] | None = Field(alias="EXPAT_DB_OPTIONS", default=None)

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
                aliased_key = f"EXPAT_{key.upper()}"
                config_dict[aliased_key] = value

        return cls(**config_dict)

    @property
    def python_log_level(self) -> str:
        return self.log_level.upper()

    def show(self) -> None:
        log_string = ""
        for key, value in self.model_dump().items():
            log_string += f"\n        {key.ljust(20, ' ')} = {value}"

        logger.info(f"Configuration loaded successfully:{log_string}\n")
