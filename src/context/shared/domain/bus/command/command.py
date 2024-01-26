import dataclasses

from context.shared.domain.bus.command.command_meta import CommandMeta


@dataclasses.dataclass(frozen=True, kw_only=True)
class Command:
    meta: CommandMeta
