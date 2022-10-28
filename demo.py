from selenium import webdriver
#from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("C:/Users/ASM/PycharmProjects/SELENIUM_Project/chromedriver")
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input").send_keys("standard_user")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.NAME,"remove-sauce-labs-backpack").click()