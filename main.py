

from selenium import webdriver
import time

driver = webdriver.Chrome('data/webdriver/chromedriver.exe')
driver.get("https://www.baidu.com/")
time.sleep(3)

driver.quit()