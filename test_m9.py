import pytest
from sanityTest import *


class TestBank:
    @pytest.fixture
    def url(self):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        return url
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test(self, driver, url):
        expected = url
        print(f'\n{url}')
        actual = openSite(driver, url)
        assert expected == actual
