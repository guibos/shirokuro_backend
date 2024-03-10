import dataclasses

from urllib3.util import Url


@dataclasses.dataclass
class Credentials:
    account_type: str
    key_id: str
    key: str
    user_id: str


@dataclasses.dataclass
class Configuration:
    scheme: str
    host: str
    port: int
    credentials: Credentials
    _well_known_path: str = "/.well-known/openid-configuration"

    @property
    def url(self) -> Url:
        return Url(scheme=self.scheme, host=self.host, port=self.port)

    @property
    def discovery_url(self) -> Url:
        return Url(scheme=self.scheme, host=self.host, port=self.port, path=self._well_known_path)
