import json

from aws_lambda_typing import events, context as context_

from apps.shared.api_controller.aws.api_controller_aws import ApiControllerAWS
from apps.shared.api_controller.aws.value_object.body import Body
from apps.shared.api_controller.aws.value_object.response import Response
from apps.shared.api_controller.aws.value_object.status_code import StatusCode
from context.account.application.creator.account_creator_command import AccountCreatorCommand
from context.account.application.creator.account_creator_command_data import AccountCreatorCommandData
from context.shared.domain.bus.command.command_meta import CommandMeta
from context.shared.infrastructure.bus.command.command_bus_sync import QueryBusSync
from context.shared.infrastructure.bus.query.query_bus_sync import CommandBusSync


class AccountCreatorPutController(ApiControllerAWS):
    """AccountCreatePutController class, """
    _DEFAULT_STATUS_CODE = StatusCode(200)

    def _manage_request(self, event: events.APIGatewayProxyEventV2, _: context_) -> Response:
        command = AccountCreatorCommand(
            data=AccountCreatorCommandData(
                account_id='a',
                username='a',
                password='b',
                email='a@a.es'
            ),
            meta=CommandMeta(
                request_id='1',
                request_timestamp='1'
            )
        )
        self._dispatch(command)

        body = {}

        return Response(
            status_code=self._DEFAULT_STATUS_CODE,
            body=Body(json.dumps(body))
        )


if __name__ == '__main__':
    query_bus = QueryBusSync()
    command_bus = CommandBusSync()


    user_create_aws_post_controller = AccountCreatorPutController(
        query_bus=query_bus,
        command_bus=command_bus
    )
