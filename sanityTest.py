from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url =" https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
def findElement(selector , driver):
    element = driver.find_element(By.CSS_SELECTOR , selector)
    return element
def openSite(driver, url):
    driver.get(url)
    time.sleep(4)
    print("The site is opened")
    return driver.current_url
