from pathlib import Path
from pydantic import BaseModel, Field


class ExpatConfig(BaseModel):
    migration_dir: Path = Field(default=Path() / "migrations")
