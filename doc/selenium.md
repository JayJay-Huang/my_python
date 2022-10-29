
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

driver = webdriver.Chrome('data/webdriver/chromedriver.exe')
driver.get("https://www.baidu.com/")
time.sleep(3)
```