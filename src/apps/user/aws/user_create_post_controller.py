import json

from aws_lambda_typing import events, context as context_

from context.shared.domain.types.uuid_type import UUIDType
from apps.shared.api_controller import ApiControllerAWS
from apps.shared.api_controller import Body
from apps.shared.api_controller import Response
from apps.shared.api_controller import StatusCode
from context.user.application.creator.user_creator_command import UserCreatorCommand


class UserCreateAWSPostController(ApiControllerAWS):
    _DEFAULT_STATUS_CODE = StatusCode(200)

    def _manage_request(self, event: events.APIGatewayProxyEventV2, _: context_) -> Response:
        user_id =  UUIDType().to_string()

        command = UserCreatorCommand(
            user_id=user_id,
            username='a',
            password='b',
            email='a@a.es'

        )
        self._dispatch(command)

        body = {
            "id": user_id,
        }

        return Response(
            status_code=self._DEFAULT_STATUS_CODE,
            body=Body(json.dumps(body))
        )


user_create_aws_post_controller = UserCreateAWSPostController(
    query_bus: QueryBus, command_bus
)
