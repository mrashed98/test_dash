from app.utils.generator import generate_random_text
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
import json


class LoginPage(PageFactory):

    locators = {
        "email_field": ("ID", 'developer_email'),
        "password_field": ('ID', 'password'),
        "login_btn": ("xpath", '//*[@id="appWrapper"]/ui-view/main/div/div/div[1]/div[2]/div/div[2]/form/button'),
    }

    def __init__(self, driver):
        self.driver = driver
        file = open('config/creds.json', 'r')
        data = json.load(file)
        self.email = data['email']
        self.password = data['password']


    def fill_valid_email(self):

        self.email_field.set_text(self.email)

    def fill_invalid_email(self):
        self.email_field.set_text(generate_random_text(8))

    def fill_valid_password(self):
        self.password_field.set_text(self.password)

    def fill_invalid_password(self):
        self.password_field.set_text(generate_random_text(5))

    def login(self):
        self.login_btn.click_button()
        try:
            container = self.driver.find_element(By.TAG_NAME, 'ibg-common-shared-account-message')
            container.find_element(By.TAG_NAME, 'button').click()
        except:
            pass