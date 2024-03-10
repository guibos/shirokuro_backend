from context.iam.shared.infrastructure.zitadel.zitadel_repository import ZitadelRepository
from context.iam.token.domain.entity.user_instropection_data import UserIntrospectionData
from context.iam.token.domain.interface.token_repository_interface.token_repository_interface import \
    TokenRepositoryInterface
from context.iam.token.domain.value_objects.access_token import AccessToken


class TokenZitadelRepository(TokenRepositoryInterface, ZitadelRepository):

    async def inspect_token(self, access_token: AccessToken) -> UserIntrospectionData:
        data = {
            "client_id": "257693441826226179",
            "token": "xcJ0V2FvGtcJObTrbphs92qsCcHPW30jP9dLI5VKDD1Td_LYfZPkKSsCZjaR3U5co5nrajM"
        }
        response = await self._client.post(str(self._discovery_data.introspection_endpoint), data=data)
        a=1