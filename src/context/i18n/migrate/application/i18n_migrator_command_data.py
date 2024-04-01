import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True)
class I18nMigratorCommandData:
    revision: str
