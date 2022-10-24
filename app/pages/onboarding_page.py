import random
from seleniumpagefactory import PageFactory
from app.utils.generator import generate_random_text


class CreateCompany(PageFactory):

    locators = {
        'create_company_btn': ('XPATH', '//*[@id="appWrapper"]/ui-view/div/div/div/div/div/div/ui-view/div/div[1]/div/div/div/div[3]/button[1]'),
        'join_company_btn': ('XPATH','//*[@id="appWrapper"]/ui-view/div/div/div/div/div/div/ui-view/div/div[1]/div/div/div/div[3]/button[2]'),
        'android_platform': ('ID', 'platform_android'),
        'notification_btn': ('ID', 'top-navbar-notifications')

    }

    def __init__(self, driver):
        self.driver = driver

    def create_new_company(self):
        self.create_company_btn.click_button()

    def join_existing_company(self):
        self.join_company_btn.click_button()

    def check_platforms(self):
        self.android_platform.visibility_of_element_located(10)


class CreateApp(PageFactory):

    locators = {
        'android_platform': ('ID', 'platform_android'),
        'ios_platform': ('ID', 'platform_IOS'),
        'company_name': ('ID', 'companyName'),
        'create_app_btn' : ('XPATH', '//*[@id="companyNameForm"]/div[2]/button')
    }

    def __init__(self, driver):
        self.driver = driver

    def change_company_name(self):
        self.company_name.clear_text()
        new_name = generate_random_text(8)
        self.company_name.set_text(new_name)

    def choose_platform(self):
        platforms = [self.android_platform, self.ios_platform]
        random_platform = random.choice(platforms)
        random_platform.click_button()

    def create_app(self):
        self.create_app_btn.click_button()

