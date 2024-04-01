from typing import List

from context.i18n.script.application.searcher.script_searcher_response_data import ScriptSearcherResponseData
from context.shared.domain.bus.query.response import Response


class ScriptSearcherResponse(Response):
    data: List[ScriptSearcherResponseData]
