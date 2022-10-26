from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.core.utils import ChromeType


class Chrome:

    def __init__(self):
        self.driver = None
        self.options = None

    def configure_driver(self, config: dict):
        self.options = ChromeOptions()
        for argument in config.values():
            self.options.add_argument(argument)

    def initialize_driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options = self.options)
        self.driver.maximize_window()
        return self.driver
