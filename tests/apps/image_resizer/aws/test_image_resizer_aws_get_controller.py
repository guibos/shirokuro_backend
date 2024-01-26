import dataclasses
import urllib.request
from urllib import request
from urllib.parse import urljoin

from pytest_bdd import given, scenario, when, then


@dataclasses.dataclass
class _DesiredSizeMother:
    width: int
    height: int



@dataclasses.dataclass
class _Response:
    content_type: str
    data: bytes


_PATH = '/'
_DESIRED_SIZES = _DesiredSizeMother(width=200, height=200)
_FILE_PATH = 'tests/context/image_resizer/fixtures/sample.png'


@scenario('../image_resizer.feature', 'Resize image in AWS')
def test_post(server: None, base_url: str):
    pass


@given('An URI of an image')
def an_image() -> bytes:
    with open(_FILE_PATH, 'rb') as f:
        return f.read()


@given('Desired sizes')
def desired_sizes() -> _DesiredSizeMother:
    return _DESIRED_SIZES


@when("I post the URI of the image and desired sizes")
def post_image(base_url: str, uri: bytes, desired_sizes: _DesiredSizeMother) -> _Response:
    full_url = urljoin(base_url, f"{_PATH}?width={desired_sizes.width}&height={desired_sizes.height}")
    req = request.Request(full_url, method='POST', data=b'')
    response = urllib.request.urlopen(req)
    return _Response(data=response.read(), content_type=response.info().content_type)


@then('I get the image with desired sizes')
def _given_a_post_request(post_image: _Response, desired_sizes: _DesiredSizeMother) -> request.Request:
    pass
