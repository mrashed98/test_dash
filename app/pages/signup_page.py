from app.utils.generator import generate_random_text
from seleniumpagefactory import PageFactory


class SignUpPage(PageFactory):
    locators = {
        "create_account_btn": ('ID', 'CreateAccountSecondDesign'),
        "accept_terms_check_box": ('XPATH',
                                   '//*[@id="appWrapper"]/ui-view/ibg-common-sign-up/main/div/div/div/div/div[1]/div[2]/form/div[5]/label'),
        "name_field": ('ID', 'developer_name'),
        "password_field": ('ID', 'developer_password'),
        "email_field": ('ID', 'developer_email'),
        "sign_up_link": (
        'XPATH', '//*[@id="appWrapper"]/ui-view/main/div/div/div[1]/div[2]/div/div[2]/form/div[5]/p/a'),
        "create_company_btn": ('XPATH',
                               '//*[@id="appWrapper"]/ui-view/div/div/div/div/div/div/ui-view/div/div[1]/div/div/div/div[3]/button[1]')
    }

    def __init__(self, driver, email, password):
        self.driver = driver
        self.valid_email = email
        self.valid_password = password

    def open(self):
        self.sign_up_link.click_button()

    def fill_valid_email(self):
        self.email_field.set_text(self.valid_email)

    def fill_invalid_email(self):
        email = generate_random_text(8)
        self.email_field.set_text(email)

    def fill_name(self):
        name = generate_random_text(8)
        self.name_field.set_text(name)

    def fill_valid_password(self):
        self.password_field.set_text(self.valid_password)

    def fill_invalid_password(self):
        pswd = generate_random_text(5)
        self.password_field.set_text(pswd)

    def accept_terms(self):
        self.accept_terms_check_box.click_button()

    def create_account(self):
        self.create_account_btn.click_button()

    def check_company(self):
        self.create_company_btn.visibility_of_element_located(10)
