from expat.db.drivers.driver import Driver

from pymysql import Connection, connect

from types import TracebackType
from typing import Self, Type, final


@final
class MySQLDriver(Driver):
    connection: Connection

    def __enter__(self) -> Self:
        print(self.config.db_password.get_secret_value())
        self.connection = connect(
            host=self.config.db_host,
            user=self.config.db_user,
            password=self.config.db_password.get_secret_value(),
            port=self.config.db_port,
            **self.config.db_options,
        )
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
