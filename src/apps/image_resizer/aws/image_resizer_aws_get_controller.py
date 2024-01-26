import json

from aws_lambda_typing import events, context as context_

from context.image_resizer.application.image_resizer_command import ImageResizerCommand
from apps.shared.api_controller import ApiControllerAWS
from apps.shared.api_controller import Body
from apps.shared.api_controller import Response
from apps.shared.api_controller import StatusCode


def image_resizer_aws_get_controller(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


class ImageResizerAWSGetController(ApiControllerAWS):
    _DEFAULT_STATUS_CODE = StatusCode(200)

    def _manage_request(self, event: events.APIGatewayProxyEventV2, _: context_) -> Response:
        command = ImageResizerCommand(
            uri='a'
        )
        self._dispatch(command)

        body = {
            "message": "Go Serverless v3.0! Your function executed successfully!",
            "input": event,
        }

        return Response(
            status_code=self._DEFAULT_STATUS_CODE,
            body=Body(json.dumps(body))
        )


