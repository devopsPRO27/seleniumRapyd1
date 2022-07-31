from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

path = '/Users/hothaifa/Desktop/chromedriver'

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

driver.get('https://www.ebay.com')
searchtb= driver.find_element(By.CSS_SELECTOR,'#gh-ac')
searchtb.send_keys('code')
searchtb.send_keys(Keys.ENTER)

driver.title
item1= driver.find_element(By.XPATH,'//*[@id="srp-river-results"]/ul/li[3]/div/div[2]/a')
item1.click()

current_handle = driver.current_window_handle
handles=driver.window_handles

known_handles=[]
known_handles.append(current_handle)

for handle in handles:
    if handle in known_handles:
        continue
    new_handle = handle
    known_handles.append(new_handle)
if new_handle != None:
    driver.switch_to.window(new_handle)
print(driver.current_url)

import pdb;pdb.set_trace()
