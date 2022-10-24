from app.test.signup_test import SignUpTest
from app.test.login_test import LoginTests
import pytest


@pytest.fixture
def test_sign_up(request):

    print("SETUP TEST")
    _tester = SignUpTest(request.param)

    def tearDown():
        print("Tear Down")
        _tester.driver.quit()

    request.addfinalizer(tearDown)

    return _tester


@pytest.fixture
def test_login(request):
    print("SETUP TEST")
    _tester = LoginTests(request.param, 'mrashed+qc@instabug.com', '01cd01e1')

    def tearDown():
        print("Tear Down")
        _tester.driver.quit()

    request.addfinalizer(tearDown)

    return _tester


class TestIt:
    @pytest.mark.parametrize('test_sign_up', ['chrome', 'firefox'], indirect=['test_sign_up'])
    def test_signup(self, test_sign_up):
        test_sign_up.test_page()
        assert 1

    @pytest.mark.parametrize('test_login', ['chrome', 'firefox'], indirect=['test_login'])
    def test_login(self, test_login):
        test_login.test_page()
        assert 1
