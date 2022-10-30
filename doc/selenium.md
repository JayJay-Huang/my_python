
## 確認瀏覽器版本
Chrome
```commandline
chrome://settings/help
```
## 下載chromedriver
```commandline
https://chromedriver.chromium.org/downloads
```
## demo
```py
from selenium import webdriver
import time
webdriver_path = 'data/webdriver/chromedriver.exe'
web_path = 'http://www.google.com'
driver = webdriver.Chrome(webdriver_path)
driver.get(web_path)
time.sleep(3)
```
## 定位
```py
el = driver.find_element_by_id()
el = driver.find_element_by_tag_name()
el = driver.find_element_by_class_name()
el = driver.find_element_by_link_text()
el = driver.find_element_by_partial_link_text()
el = driver.find_element_by_xpath()
el = driver.find_element_by_css_selector()
```
undown
```commandline
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
```