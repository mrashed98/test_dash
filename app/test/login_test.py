from app.pages.login_page import LoginPage
from app.pages.dashboard_page import DashboardPage
import logging
import pytest


@pytest.mark.order(3)
class TestLogin:

    @pytest.mark.parametrize('props', ['chrome', 'firefox'], indirect=['props'])
    def test_page(self, props):

        dashboards = props.dashboards
        driver = props.browser

        for url in dashboards:
            try:
                driver.get(url)
                page = LoginPage(driver)
                self.automate_run(page)
                page = DashboardPage(driver)
                page.logout()
                assert 1
            except Exception:
                logging.exception(f"Error occurred with dashboard {url}")
                assert 0

    def automate_run(self, dashboard):

        dashboard.fill_valid_email()
        dashboard.fill_valid_password()
        dashboard.login()


