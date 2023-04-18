from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

customerSelector =" body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button"
customerNameSelector = "#userSelect"
selectedName = "#userSelect > option:nth-child(4)"
sidePageSelector = "body > div > div > div.ng-scope"
loginButtonSelector = "body > div > div > div.ng-scope > div > form > button"
depositButtonSelector = "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)"
typeAmountSelector = "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input"
depositAmount = "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button"
balanceSelector = "body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)"

def getBalance( driver):
    balance = findElement(balanceSelector, driver)
    balance = (float)(balance.text)
    return balance
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
def depositBankUser(driver , amount  ):
    depositButton = findElement(depositButtonSelector, driver)
    clickElement(depositButton)
    typeAmount = findElement(typeAmountSelector, driver)
    typeAmount.send_keys(amount)
    currentBalance = getBalance(driver)
    deposit = findElement(depositAmount, driver)
    clickElement(deposit)
    return currentBalance




