import pytest
from deposit750Total import *
from deposit250 import *
from selenium import webdriver

class TestUserBank:
    @pytest.fixture
    def amountDeposit(self):
        amount= "1000"
        return amount
    @pytest.fixture
    def amountWithdraw(self):
        amount = "250"
        return amount
    @pytest.fixture
    def url(self):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        return url
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_deposit250(self, driver, url, amountDeposit):
        openSite(driver, url)
        loginUserBank(driver)
        balanceBefore = depositBankUser(driver, amountDeposit)
        balanceAfter = getBalance(driver)
        amount = float(amountDeposit)
        assert balanceAfter == balanceBefore + amount

