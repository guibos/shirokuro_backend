from abc import abstractmethod, ABC
from typing import Dict, Union

from aws_lambda_typing import events, context as context_

from context.shared.domain.bus.command.command_bus import CommandBus
from context.shared.domain.bus.query.query_bus import QueryBus
from apps.shared.api_controller._api_controller_base import ApiControllerBase
from apps.shared.api_controller._api_exception_http_status_code_mapping import \
    ApiExceptionHttpStatusCodeMapping
from apps.shared.api_controller.aws.value_object.response import Response


class ApiControllerAWS(ApiControllerBase, ABC):
    def __init__(self, query_bus: QueryBus, command_bus: CommandBus,
                 exception_handler: ApiExceptionHttpStatusCodeMapping):
        super().__init__(query_bus, command_bus)

    def __call__(self, event: events.APIGatewayProxyEventV2, context: context_) -> Dict[str, Union[str, int]]:
        # TODO: implement exception handler.
        response = self._manage_request(event, context)

        return {
            "statusCode": response.status_code,
            "body": response.body
        }

    @abstractmethod
    def _manage_request(self, event: events.APIGatewayProxyEventV2, context: context_) -> Response:
        pass


