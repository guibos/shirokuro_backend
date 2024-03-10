import httpx
from authlib.integrations.httpx_client import AsyncAssertionClient

from context.iam.shared.infrastructure.oidc.value_object.openid_connect_discovery_data import \
    OpenIDConnectDiscoveryData
from context.iam.shared.infrastructure.zitadel.value_obkect.configuration import Configuration


class ZitadelRepository:
    _ADMIN_SCOPE = 'openid profile email address urn:zitadel:iam:org:project:id:zitadel:aud'

    def __init__(self, client: AsyncAssertionClient, discovery_data: OpenIDConnectDiscoveryData):
        self._client = client
        self._discovery_data = discovery_data

    @classmethod
    async def create(cls, configuration: Configuration) -> 'ZitadelRepository':
        async with httpx.AsyncClient() as client:
            response = await client.get(configuration.discovery_url.url)

        discovery_data = OpenIDConnectDiscoveryData(**response.json())

        header = {
            'alg': discovery_data.token_endpoint_auth_signing_alg_values_supported[-1],
            "kid": configuration.credentials.key_id
        }

        client = AsyncAssertionClient(
            token_endpoint=str(discovery_data.token_endpoint),
            issuer=configuration.credentials.user_id,
            subject=configuration.credentials.user_id,
            audience=configuration.url.url,
            scope=cls._ADMIN_SCOPE,
            key=configuration.credentials.key,
            header=header
        )

        return cls(client, discovery_data)
