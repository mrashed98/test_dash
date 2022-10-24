import logging

from app.pages.onboarding_page import CreateCompany, CreateApp
from app.pages.signup_page import SignUpPage
import pytest
from selenium.common.exceptions import NoSuchElementException
from app.utils.generator import get_creds


@pytest.mark.order(1)
class TestSignUp:

    @pytest.mark.parametrize('props', ['chrome', 'firefox'], indirect=['props'])
    def test_sign_up_page(self, props):

        dashboards = props.dashboards
        driver = props.browser

        email, password = get_creds()

        for url in dashboards:
            try:
                driver.get(url)
                page = SignUpPage(driver, email, password)
                self.automate_input(page)
                create_company = CreateCompany(driver)
                create_company.create_new_company()
                create_app = CreateApp(driver)
                create_app.change_company_name()
                create_app.choose_platform()
                create_app.create_app()
                assert 1
            except Exception:
                logging.exception(f"Error occurred with dashboard {url}")
                assert 0

    def automate_input(self, dashboard):
        dashboard.open()
        dashboard.fill_valid_email()
        dashboard.fill_name()
        dashboard.fill_valid_password()
        try:
            dashboard.accept_terms()
        except NoSuchElementException:
            pass
        dashboard.create_account()


