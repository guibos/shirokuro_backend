from typing import List

from context.internationalization.script.domain.aggregate.script import Script


class ScriptRepository:
    def search(self, query: str) -> List[Script]:
        pass
    def create(self, script: Script) -> Script:
        raise NotImplementedError

    def update(self, script: Script) -> Script:
        raise NotImplementedError
