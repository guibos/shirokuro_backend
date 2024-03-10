from abc import ABC, abstractmethod

from context.iam.token.domain.entity.user_instropection_data import UserIntrospectionData
from context.iam.token.domain.value_objects.access_token import AccessToken


class TokenRepositoryInterface(ABC):
    @abstractmethod
    async def inspect_token(self, access_token: AccessToken) -> UserIntrospectionData:
        raise NotImplementedError
