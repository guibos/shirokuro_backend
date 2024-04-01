import traceback
from abc import abstractmethod, ABC
from typing import Any

from context.shared.application.application.application import Application
from context.shared.domain.bus.query.query import Query
from context.shared.domain.bus.query.response import Response
from context.shared.domain.bus.query.response_error_data import ResponseErrorData
from context.shared.domain.exception.security.child.forbidden_error import ForbiddenError
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata


class ApplicationQuery(Application, ABC):
    async def query(self, query: Query) -> Response:
        try:
            request_metadata = self._get_request_metadata_value_object(query.request_metadata)
            await self._check_roles(request_metadata)
            return await self._query(query.data, request_metadata)
        except ForbiddenError:
            self._logger.exception("Unauthorized.")
            return Response(
                ok=False,
                errors=[
                    ResponseErrorData(
                        internal=True,
                        message='Unauthorized.',
                        traceback=traceback.format_exc())],
                data=[]
            )
        except Exception:
            self._logger.exception("Unexpected error.")
            return Response(
                ok=False,
                errors=[
                    ResponseErrorData(
                        internal=True,
                        message='Internal error.',
                        traceback=traceback.format_exc())],
                data=[]
            )

    @abstractmethod
    async def _query(self, query_data: Any, metadata: RequestMetadata) -> Response:
        raise NotImplementedError
