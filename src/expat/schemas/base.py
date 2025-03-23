from expat.utils import strip_empty_dicts

from pydantic import BaseModel
from tomlkit import dumps, loads

from abc import abstractmethod
from typing import Any, Self, Type


class Base(BaseModel): ...


class BaseToml(Base):
    @classmethod
    def model_load_toml(cls: Type[Self], data: str) -> Self:
        return cls(**loads(data))

    def model_dump_toml(self, strip_dict: bool = True) -> str:
        raw_dict = self.model_dump(mode="json")
        sorted_dict = {k: raw_dict[k] for k in self.table_sort_order}

        processed_dict = self.toml_dump_hook(sorted_dict)

        if strip_dict:
            stripped_dict = strip_empty_dicts(processed_dict)

        return dumps(stripped_dict)

    @property
    @abstractmethod
    def table_sort_order(self) -> list[str]: ...

    def toml_dump_hook(self, dumped: dict[Any, Any]) -> dict[Any, Any]:
        return dumped
