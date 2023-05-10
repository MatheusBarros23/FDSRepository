from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Create your tests here.
class TestHome(LiveServerTestCase):
    driver = webdriver.Chrome(options=chrome_options)
    def test_title(self):
        self.driver.get('http://127.0.0.1:8000/')
        assert "The install worked" in self.browser.title

    def test_href(self):
        self.driver.get('http://127.0.0.1:8000/')
        link = self.driver.find_element(By.CLASS_NAME, 'logo')
        assert link.get_attribute('href') == 'https://www.djangoproject.com/'
