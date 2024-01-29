import json

from aws_lambda_typing import events, context as context_

from apps.aws.bootstrap import query_bus, command_bus
from apps.aws.shared.api_controller_aws.api_controller_aws import ApiControllerAWS
from apps.aws.shared.api_controller_aws.value_object.body import Body
from apps.aws.shared.api_controller_aws.value_object.response import Response
from apps.aws.shared.api_controller_aws.value_object.status_code import StatusCode
from context.user.account.application.creator import AccountCreatorCommand
from context.user.account.application.creator import AccountCreatorCommandData
from context.shared.domain.bus.command.command_meta import CommandMeta


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
    account_create_aws_post_controller = AccountCreatorPutController(
        query_bus=query_bus,
        command_bus=command_bus
    )
