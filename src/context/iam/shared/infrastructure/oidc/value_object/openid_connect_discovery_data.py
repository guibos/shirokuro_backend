from typing import Annotated, List

from pydantic import BaseModel, Field
from pydantic_core import Url


class OpenIDConnectDiscoveryData(BaseModel):
    issuer: Annotated[Url, Field(examples=['http://localhost:8080'])]
    authorization_endpoint: Annotated[
        Url, Field(examples=["http://localhost:8080/oauth/v2/authorize"])]
    token_endpoint: Annotated[
        Url, Field(examples=["http://localhost:8080/oauth/v2/token"])]
    introspection_endpoint: Annotated[
        Url,
        Field(examples=["http://localhost:8080/oauth/v2/introspect"])]
    userinfo_endpoint: Annotated[
        Url, Field(examples=["http://localhost:8080/oidc/v1/userinfo"])]
    revocation_endpoint: Annotated[
        Url, Field(examples=["http://localhost:8080/oauth/v2/revoke"])]
    end_session_endpoint: Annotated[
        Url,
        Field(examples=["http://localhost:8080/oidc/v1/end_session"])]
    device_authorization_endpoint: Annotated[
        Url,
        Field(
            examples=["http://localhost:8080/oauth/v2/device_authorization"])]
    jwks_uri: Annotated[Url,
    Field(
        examples=["http://localhost:8080/oauth/v2/keys"])]
    scopes_supported: Annotated[
        List[str],
        Field(examples=[
            "openid", "profile", "email", "phone", "address", "offline_access"
        ])]
    response_types_supported: Annotated[
        List[str],
        Field(examples=["code", "id_token", "id_token authenticate"])]
    grant_types_supported: Annotated[
        List[str],
        Field(examples=[
            "authorization_code", "implicit", "refresh_token",
            "client_credentials",
            "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "urn:ietf:params:oauth:grant-type:device_code"
        ])]
    subject_types_supported: Annotated[List[str], Field(examples=["public"])]
    id_token_signing_alg_values_supported: Annotated[List[str],
    Field(examples=["RS256"])]
    request_object_signing_alg_values_supported: Annotated[
        List[str], Field(examples=["RS256"])]
    token_endpoint_auth_methods_supported: Annotated[
        List[str],
        Field(examples=[
            "none", "client_secret_basic", "client_secret_post",
            "private_key_jwt"
        ])]
    token_endpoint_auth_signing_alg_values_supported: Annotated[
        List[str], Field(examples=["RS256"])]
    revocation_endpoint_auth_methods_supported: Annotated[
        List[str],
        Field(examples=[
            "none", "client_secret_basic", "client_secret_post",
            "private_key_jwt"
        ])]
    revocation_endpoint_auth_signing_alg_values_supported: Annotated[
        List[str], Field(examples=["RS256"])]
    introspection_endpoint_auth_methods_supported: Annotated[
        List[str],
        Field(examples=["client_secret_basic", "private_key_jwt"])]
    introspection_endpoint_auth_signing_alg_values_supported: Annotated[
        List[str], Field(examples=["RS256"])]
    claims_supported: Annotated[
        List[str],
        Field(examples=[
            "sub", "aud", "exp", "iat", "iss", "auth_time", "nonce", "acr",
            "amr", "c_hash", "at_hash", "act", "scopes", "client_id", "azp",
            "preferred_username", "name", "family_name", "given_name",
            "locale", "email", "email_verified", "phone_number",
            "phone_number_verified"
        ])]
    code_challenge_methods_supported: Annotated[List[str],
    Field(examples=["S256"])]
    ui_locales_supported: Annotated[
        List[str],
        Field(examples=[
            "bg", "cs", "de", "en", "es", "fr", "it", "ja", "mk", "nl", "pl",
            "pt", "ru", "zh"
        ])]
    request_parameter_supported: Annotated[bool, Field(examples=[True])]
    request_uri_parameter_supported: Annotated[bool, Field(examples=[False])]
