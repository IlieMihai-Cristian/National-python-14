import datetime
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get('http://127.0.0.1:8003/')
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys('mihai')
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys('admin')
        submit = self.driver.find_element(by=By.CLASS_NAME, value='btn-success')
        submit.submit()
        self.logs = open('logs.txt', 'a')

    def test_form(self):
        self.logs.write(f'Test Login Page {datetime.datetime.now()}\n')
        if '' in self.driver.page_source:
            value = True
        else:
            value = False
        self.logs.write(f' - Existing page check: {value}\n')
        try:
            if self.driver.find_element(by=By.CLASS_NAME, value='errorlist'):
                value = False
        except Exception:
            value = True
        self.logs.write(f' - Password and username check: {value}\n')
        assert value
