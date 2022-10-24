import pytest
from app.pages.login_page import LoginPage
from app.pages.dashboard_page import DashboardPage
import logging


@pytest.mark.order(4)
class TestDashboard:

    @pytest.mark.parametrize('props', ['firefox', 'chrome'], indirect=['props'])
    def test_page(self, props):

        dashboards = props.dashboards
        driver = props.browser

        for url in dashboards:
            try:
                driver.get(url)
                self.login(driver)
                page = DashboardPage(driver)
                self.automate_run(page)
                assert 1
            except Exception:
                logging.exception(f"ERROR OCCURRED IN DASHBOARD --> {url}")
                assert 0

    def login(self, driver):
        page = LoginPage(driver)
        page.fill_valid_email()
        page.fill_valid_password()
        page.login()

    def automate_run(self, page):
        page.choose_app()
        page.visit_releases_page()
        page.check_update_btn()
        page.check_docs_btn()
        page.check_notification_btn()
        page.logout()

