from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
s = Service("C:/Users/ASM/Desktop/Automation _Code/SELENIUM/chromedriver")
#print(s.path)
driver = webdriver.Chrome(executable_path=s.path)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"/html/body/div/div/header/div/div[2]/form/input").send_keys("Mushroom")
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div/div[2]/a[2]").click()