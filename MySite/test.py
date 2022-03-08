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
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=webdriver.DesiredCapabilities.CHROME)
    
    def test_parrafos(self):
        #webApp = os.environ['WEBAPP_HOST']
        driver = self.driver
        driver.get("http://172.19.0.2:8080/AppWeb/index.html")
        time.sleep(5)
        paragraphs = driver.find_elements_by_tag_name('p')
        for paragraph in paragraphs:
            assert "This is a paragraph." in paragraph.text
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()