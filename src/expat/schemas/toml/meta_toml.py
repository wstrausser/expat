from expat.schemas.base import BaseToml

from pydantic import AwareDatetime

from datetime import datetime, UTC
from importlib.metadata import version
from typing import final
from uuid import uuid4


@final
class MetaToml(BaseToml):
    created_time: AwareDatetime = datetime.now(UTC)
    id: str = uuid4().hex
    expat_version: str = version("expat")

    @property
    def table_sort_order(self) -> list[str]:
        return ["created_time", "id", "expat_version"]
