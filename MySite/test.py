import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os 


class html_unittest(unittest.TestCase):
    def setUp(self):
        host = os.environ['SELENIUM_REMOTE_HOST']
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor='http://172.18.0.4:4444/wd/hub', options=chrome_options)
    
    def test_parrafos(self):
        webApp = os.environ['WEBAPP_HOST']
        driver = self.driver
        driver.get("http://172.18.0.3:8080/AppWeb/index.html")
        time.sleep(3)
        paragraphs = driver.find_elements_by_tag_name('p')
        for paragraph in paragraphs:
            assert "This is a paragraph." in paragraph.text
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()