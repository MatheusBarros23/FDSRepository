from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
class TestHome(LiveServerTestCase):
    self.driver.get('http://127.0.0.1:8000/')
    assert "The install worked" in self.browser.title
def test_href(self):
    self.driver.get('http://127.0.0.1:8000/')
    link = self.driver.find_element(By.CLASS_NAME, 'logo')
    assert link.get_attribute('href') == 'https://www.djangoproject.com/'
