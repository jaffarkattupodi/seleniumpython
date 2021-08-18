from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
def test_01():
    driver=webdriver.Chrome()
    driver.get('https://www.amazon.in/')
    driver.find_element(By.ID,'twotabsearchtextbox').send_keys('mobiles')
    driver.find_element(By.ID,'twotabsearchtextbox').send_keys(Keys.ENTER)
