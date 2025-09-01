from expat.utils import hash_file

from pathlib import Path
from pydantic import BaseModel
from typing import Self, Type


class Migration(BaseModel):
    migration_path: Path
    migration_id: str
    migration_name: str
    up_hash: str
    down_hash: str


    @classmethod
    def from_path(cls: Type[Self], path: Path) -> Self:
        migration_id, migration_name = path.name.split("_", 1)

        migration = cls(
            migration_path=path,
            migration_id=migration_id,
            migration_name=migration_name,
            up_hash=hash_file(path / "up.sql"),
            down_hash=hash_file(path / "down.sql"),
        )

        return migration
