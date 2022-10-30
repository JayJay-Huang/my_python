from selenium import webdriver
import time
webdriver_path = 'data/webdriver/chromedriver.exe'
web_path = 'http://www.google.com'
driver = webdriver.Chrome(webdriver_path)
driver.get(web_path)

# e1 = driver.find_element_by_class_name('gLFyf')
e1 = driver.find_element_by_xpath("//div[@class='gLFyf']")
e1.send_keys('Selenium Python666')

time.sleep(3)