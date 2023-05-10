from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Documentação selenium para Python: https://selenium-python.readthedocs.io/
# Exemplos: https://ordinarycoders.com/blog/article/testing-django-selenium

# Create your tests here.

class TestHome(LiveServerTestCase):
    def test_title(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')
        assert "The install worked" in browser.title
        browser.quit()

    def test_href(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/')
        link = browser.find_element(By.CLASS_NAME, 'logo')
        assert link.get_attribute('href') == 'https://www.djangoproject.com/'
        browser.quit()
