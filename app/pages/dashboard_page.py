from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(PageFactory):

    locators = {
        "app_overview_btn": ('XPATH', '//*[@id="c-sidebar"]/ul/li[1]'),
        "releases_btn": ('XPATH', '//*[@id="c-sidebar"]/ul/li[2]'),
        "apps_dropdown": ('tag', 'ibg-common-app-switcher'),
        "updates_btn": ('ID', 'top-navbar-product-updates'),
        "docs_btn": ('ID', 'top-navbar-docs'),
        "notification_btn": ('ID', 'top-navbar-notifications'),
    }

    def __init__(self, driver):
        self.driver = driver

    def choose_app(self):
        self.apps_dropdown.click_button()
        app_list = self.driver.find_element(By.TAG_NAME, 'pane')
        apps = app_list.find_elements(By.TAG_NAME, 'li')
        apps[0].click()

    def visit_app_overview(self):
        self.app_overview_btn.click_button()

    def visit_releases_page(self):
        self.releases_btn.click_button()

    def check_update_btn(self):
        self.updates_btn.visibility_of_element_located(30)

    def check_docs_btn(self):
        self.docs_btn.visibility_of_element_located(30)

    def check_notification_btn(self):
        self.notification_btn.visibility_of_element_located(30)

    def get_account_dropdown(self):
        menu_container = self.driver.find_element(
            By.TAG_NAME, 'ibg-common-top-navbar-menu')
        menu_list = menu_container.find_elements(By.TAG_NAME, 'li')
        account_dropdown = menu_list[-1]
        return account_dropdown

    def logout(self):
        account_dropdown = self.get_account_dropdown()
        account_dropdown.click()
        management_list = self.driver.find_element(By.TAG_NAME, 'pane')
        items = management_list.find_elements(By.TAG_NAME, 'li')
        items[-1].click()
