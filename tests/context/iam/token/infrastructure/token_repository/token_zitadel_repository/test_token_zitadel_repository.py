import pytest

from context.iam.shared.infrastructure.zitadel.value_obkect.configuration import Configuration, Credentials
from context.iam.token.domain.value_objects.access_token import AccessToken
from context.iam.token.infrastructure.token_repository.token_zitadel_repository.token_zitadel_repository import \
    TokenZitadelRepository


@pytest.mark.asyncio
async def test_introspect_token_zitadel_repository():
    repo = await TokenZitadelRepository.create(
        configuration=Configuration(
            scheme='http',
            host='localhost',
            port=8080,
            credentials=Credentials(
                account_type='serviceaccount',
                key_id='257654100680769539',
                key='-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAtTYmcQwxU0dd9qZyaRpJ73HdBIeXfiAI9ycIM3cA+0cG4IBx\n3o4YsUFr+dzjg9DhRBtun6f9lT5wA2o8NHkUHC5k9dT5rbdjRYMGk4Q+rI9ncoxh\nONeFn1akY3Vw6sghoLvM0+X7XgOpp/DFU7S+nkqCQSy/NdOyW4YZCcSWifuPteJB\nsRfIpnc9WqM5DoktASL2GeFS6kMbeujRZlftli6Ks/mmKAZUCvuEoX71jKnu6eyL\ngj5m3plR4U5mbz7D1mFqel60eVreOQibGrEDMu4cvtskp6NY8i1y0upaRambNFXi\nLoZXxj78jDen1wsLkuRoSk5uqBGykzH/5y4xawIDAQABAoIBAQCJ29JO+pmj441m\nkaZEs01ALn2YbpcfyrtHW5hvnr9OavCeZtk6GRxL7Zt5kUQ9CfH2YHA+Yg0XN1L8\nJhv7R4m3DsycARSZxgRt44pjO556pPZsPMPR/JSZbc7OI5Bt7Sc4Iudm5XXgRiUR\nsKhOUBkcT07cynAFQTJVUqVFuxtTiJerL+1mDKEjVa4xc07D8lxaj2e4bXVGM9Tu\nCWYyxPO9iI/6+N3YqL1D6SpaLkcPLFcOmo5BGlZS8zojmG7yToahoxccxevH9nFK\nFsI1ARTRl52lDFDepR3rEGFLbyU6wkCIfuy9+rvNgYYH0avYYL6rfcJ5lOzJJZ2M\nNPuedVtRAoGBAMqAHe9nQJ27q2xWSPaaTPl2f8EnZrsLg2iedBA3om6LSbSvNp8l\nfXzq/9RlMG0aWY+qRjQaTquSMTeg5hoFVWriHVO8xaCSAGlGlM92oErjCg/tYShR\nuSEQiE1SwK6SGO34KuFeXqndEVrviTMlWD7j6F7sO72KfVbgIdC19+FdAoGBAOUW\nLlZYSgBpzQ0bOX1Uu921B6XoqnBV6BI7R6QWy+QESg0n+G7f6gcxCbw7unyBnjtP\n3eSo/RMAM5SYHQhy1o9zqAjmAxgAcJSYCtfU43mVpaNUev4TkN+oeaJapbLBv+Ce\nOyPTiUdSF2vlvOK/ntIVepVr9cMBChnS3TWH+0lnAoGANFFNaqDejOIDtAXG7A+J\ne5ol/51SaVjcJpdpnRcCnFTYQhpSnmNtPGzqk9Fg5Y89PGTdpnB1itZGaPzk9iwS\nmX653PyUgpu2B3z4zXD0kOR/oQXPaD9U+TnwPSn4JiIQ1sqbKYbcJj67USc550Dq\nv7TaQEwAU0QIhf16PxYEaPECgYA50OtI52dly03w7NoJg4UWY0XW3W2GhGfZkhR2\nmTpEBcEaqOfOM7zAq+OlGf3qxlvE5FdAClY0oWxjKDDLnRABjFLwS/yj5hiDqAu0\nhQoT+WygWAXicdWyXLa1/uKqxrNCYSzT0eNnmJRIquaM44eVxc32QBT6bhy6f7lM\ndVE6KQKBgQCO31U5+olggjl50uPJJ417KxyoQ0TURwOp9gwcmyVEXnVpEo0DGJf+\nR3k1T4hT0sz/0vhTDb7b5JCy3pHWiVZLVYu3feAtHPebHUCPVocXLj+K2NGkeMH4\nxwpwA8fVru42OlCQ5E2mOsIbcJFXuH/j8vT7msC1UpgbsCzljV5ScQ==\n-----END RSA PRIVATE KEY-----\n',
                user_id='257654065515724803'
            )
        )
    )

    await repo.inspect_token(access_token=AccessToken('reXKZxUVGoIW5yXnWrFFmsw4DlRK3NPVkO2cHYV_YENhJQioDDdO1oDqzWkA0MluOxISc1U'))
