import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import creds
import json
import requests
import re
from HTMLParser import HTMLParser


class MessageFB(unittest.TestCase):
    username = None
    message = None

    def setUp(self):
        chrome_opt = webdriver.ChromeOptions()

        prefs = {'profile.default_content_settings_views.notification': 2}
        chrome_opt.add_experimental_option('prefs', prefs)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        # self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
        self.driver.implicitly_wait(10)
        self.base_url = 'https://www.facebook.com/'
        self.message = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1')
        clean = re.compile('<.*?>')
        self.message = re.sub(clean, '', json.loads(self.message.text, encoding='utf-8')[0]['content'])
        parser = HTMLParser()
        self.message = parser.unescape(self.message)

    def tearDown(self):
        self.driver.close()

    def _login(self):
        """Login facebook app"""
        driver = self.driver
        driver.get(self.base_url + 'login')
        email_field = driver.find_element(By.XPATH, "//input[@id='email']")
        email_field.send_keys(creds.FB_USERNAME)
        pwd_field = driver.find_element(By.XPATH, "//input[@id='pass']")
        pwd_field.send_keys(creds.FB_PASSWORD)
        pwd_field.send_keys(Keys.ENTER)

    def test_message(self):
        driver = self.driver
        self._login()
        if self.username:
            message_url = '{}{}'.format(
                self.base_url, 'messages/' + str(self.username))
            driver.get(message_url)
            text_field = driver.find_element(By.XPATH, "//div//textarea[@role='textbox']")
            text_field.send_keys(self.message)
            text_field.send_keys(Keys.ENTER)
        else:
            pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        MessageFB.username = sys.argv.pop()
    unittest.main()
