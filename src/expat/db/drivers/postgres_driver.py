from expat.db.drivers.driver import Driver

from psycopg import Connection, connect

from types import TracebackType
from typing import Self, Type, final
from urllib.parse import urlencode


@final
class PostgresDriver(Driver):
    connection: Connection

    def __enter__(self) -> Self:
        self.connection = connect(self.connection_string)
        return self

    def __exit__(
        self,
        exception_type: Type[BaseException] | None,
        exception: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if exception is not None:
            self.connection.rollback()

        else:
            self.connection.commit()

        self.connection.close()

    @property
    def connection_string(self) -> str:
        if self.config.db_options is not None:
            options_string = f"?{urlencode(self.config.db_options)}"
        else:
            options_string = ""

        return (
            f"postgresql://{self.config.db_user}:"
            f"{self.config.db_password.get_secret_value()}@{self.config.db_host}:"
            f"{self.config.db_port}/{self.config.db_database}{options_string}"
        )

    def create_expat_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                    CREATE SCHEMA expat;
                """
            )

    def destroy_expat_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                    DROP SCHEMA expat;
                """
            )
