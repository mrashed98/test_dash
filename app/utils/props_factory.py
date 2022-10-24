from app.factory.factory import Factory as DriverFactory
import json


class PropsFactory:

    def __init__(self, browser_name):
        self.driver_factory = DriverFactory('config/browsers_config.json')
        self.browser = self.driver_factory.get_driver(browser_name)
        self.browser.implicitly_wait(10)
        self.dashboards = self.get_dashboards()

    def get_dashboards(self):
        raw_data = open('config/dashboard_urls.json', 'r')
        dashboards = json.load(raw_data)
        return dashboards.values()

    def tear_down(self):
        self.browser.quit()
