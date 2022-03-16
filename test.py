import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os 


class html_unittest(unittest.TestCase):
    def setUp(self):
        #host = os.environ['SELENIUM_REMOTE_HOST']
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
        browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
        browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
        caps = {
            'os': 'Windows',
            'browser': 'chrome',
            'browserstack.local': browserstack_local,
            'browserstack.localIdentifier': browserstack_local_identifier,
            'browserstack.user': username,
            'browserstack.key': access_key
        }
        driver = webdriver.Remote(command_executor='https://hub-cloud.browserstack.com/wd/hub',desired_capabilities=caps)
    
    def test_parrafos(self):
        #webApp = os.environ['WEBAPP_HOST']
        driver = self.driver
        driver.get("http://locahost:8080/AppWeb/index.html")
        time.sleep(5)
        paragraphs = driver.find_elements_by_tag_name('p')
        for paragraph in paragraphs:
            assert "This is a paragraph." in paragraph.text
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()