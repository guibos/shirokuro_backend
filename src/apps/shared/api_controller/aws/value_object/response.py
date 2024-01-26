import dataclasses

from apps.shared.api_controller.aws.value_object.body import Body
from apps.shared.api_controller.aws.value_object.status_code import StatusCode


@dataclasses.dataclass
class Response:
    status_code: StatusCode
    body: Body
