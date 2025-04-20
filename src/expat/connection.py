from __future__ import annotations

from typing import Any, Protocol


class DBAPIConnection(Protocol):
    def cursor(self, *args, **kwargs) -> DBAPICursor:
        ...

    def commit(self) -> None:
        ...

    def close(self) -> None:
        ...

class DBAPICursor(Protocol):
    def execute(self, query: Any, params: Any = None) -> None:
        ...

    def close(self) -> None:
        ...

