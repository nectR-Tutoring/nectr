from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Browser(object):
    base_url = 'http://localhost:8000'
    driver = webdriver.Remote(
        command_executor='http://phantomjs:8901',
        desired_capabilities=DesiredCapabilities.PHANTOMJS)
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)
