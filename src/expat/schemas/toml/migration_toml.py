from expat.schemas.base import Base, BaseToml

from typing import final


@final
class ScriptsConfig(Base):
    apply_scripts: list[str] = ["./up.sql"]
    rollback_scripts: list[str] = ["./down.sql"]


@final
class MigrationConfig(Base):
    label: str
    comment: str
    apply_in_prod: bool = True
    split_commands: bool = True
    scripts: ScriptsConfig = ScriptsConfig()


@final
class MigrationToml(BaseToml):
    migration: MigrationConfig

    @property
    def table_sort_order(self) -> list[str]:
        return ["migration"]
