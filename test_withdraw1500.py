import pytest
from withdraw1500 import *
from selenium import webdriver
class TestUserBank:
    @pytest.fixture
    def transactionType(self):
        type = "Debit"
        return type

    @pytest.fixture
    def amountWithdraw(self):
        amount = "1500"
        return amount
    @pytest.fixture
    def url(self):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        return url
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver
    def test_withdraw(self , driver, url , amountWithdraw, transactionType):
        openSite(driver, url)
        loginUserBank(driver)
        withdrawBankUser(driver, "1500")
        transactionButton = findElement(transactionButtonSelector, driver)
        clickElement(transactionButton)
        dateTimeBtn = findElement(dateTimeButtonSelector, driver)
        clickElement(dateTimeBtn)
        amountValue = findElement(amountSelectorValue, driver)
        currenyType = findElement(transactionTypeSelector, driver)
        time.sleep(2)
        assert amountValue.text == amountWithdraw and currenyType.text == transactionType






