from selenium import webdriver
import re
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

driver.find_element_by_id("email").send_keys("username")
driver.find_element_by_id('pass').send_keys("password")
driver.find_element_by_id('loginbutton').click()

