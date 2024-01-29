import urllib.request
from urllib.parse import urljoin

from pytest_bdd import scenario, given, when, then

from tests.context.user.account.domain.value_object.account_id_mother import AccountIdMother
from tests.context.user.account.domain.value_object.password_mother import PasswordMother


@scenario('account_creator_put_controller.feature', 'Create account')
def test_post(server: None, base_url: str):
    pass


@given('account_id', target_fixture='account_id')
def account_id() -> str:
    return AccountIdMother.create().to_string()


@given('email', target_fixture='email')
def email() -> str:
    return ''


@given('password', target_fixture='password')
def password() -> str:
    return PasswordMother().create().to_string()


@when("I put data to the api", target_fixture="put_data")
def put_data(base_url: str, account_id: str, email: str, password: str, ):
    full_url = urljoin(base_url, "/")
    req = urllib.request.Request(full_url, method='PUT', data=b'')
    response = urllib.request.urlopen(req)
    return response


@then('I get a 200 or 202 http response')
def _given_a_post_request(put_data):
    pass