from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
customerSelector =" body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button"
customerNameSelector = "#userSelect"
selectedName = "#userSelect > option:nth-child(2)"
sidePageSelector = "body > div > div > div.ng-scope"
loginButtonSelector = "body > div > div > div.ng-scope > div > form > button"
depositButtonSelector = "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)"
typeAmountSelector = "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input"
depositAmount = "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button"
balanceSelector = "body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)"
withdrawButtonSelector = "button.btn-lg:nth-child(3)"
typeWithdrawAmount = ".form-control"
withdrawAmountButton = ".btn-default"
transactionButtonSelector = "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)"
dateTimeButtonSelector = "body > div > div > div.ng-scope > div > div:nth-child(2) > table > thead > tr > td:nth-child(1) > a"
amountSelectorValue = "#anchor0 > td:nth-child(2)"
transactionTypeSelector ="#anchor0 > td:nth-child(3)"
def clickElement(element ):
    element.click()
    time.sleep(2)
def findElement(selector , driver):
    element = driver.find_element(By.CSS_SELECTOR , selector)
    return element
def openSite(driver, url):
    driver.get(url)
    print("Loading the page")
    time.sleep(3)
def loginUserBank(driver):
    customerButton = findElement(customerSelector, driver)
    clickElement(customerButton)
    customerName = findElement(customerNameSelector, driver)
    clickElement(customerName)
    optionName = findElement(selectedName, driver)
    clickElement(optionName)
    sidePage = findElement(sidePageSelector, driver)
    clickElement(sidePage)
    loginButton = findElement(loginButtonSelector, driver)
    clickElement(loginButton)

def withdrawBankUser(driver , amount):
    withdrawButton = findElement(withdrawButtonSelector, driver)
    clickElement(withdrawButton)
    typeAmount = findElement(typeWithdrawAmount , driver)
    typeAmount.send_keys(amount)
    withdrawAmount = findElement(withdrawAmountButton, driver)
    clickElement(withdrawAmount)
