import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

path = '/Users/hothaifa/Desktop/chromedriver'

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

driver.get('https://www.ebay.com')
search_tb = driver.find_element(by=By.CSS_SELECTOR, value='#gh-ac')
search_tb.send_keys('Dragon ball')
search_tb.send_keys(Keys.ENTER)

item1 = driver.find_element(By.CSS_SELECTOR,
                            '#srp-river-results > ul > li:nth-child(1) > div > div.s-item__image-section > div > a > div > img')

item1.click()

main_handler = driver.current_window_handle
# this is the main window handle

list_of_handles = driver.window_handles
list_of_known_handles=[main_handler]
for handle in list_of_handles :
    if handle not in list_of_known_handles:
        new_handle = handle
        list_of_known_handles.append(new_handle)
        break
driver.switch_to.window(new_handle)
print(driver.title)
driver.switch_to.window(main_handler)
driver.save_screenshot('screen1.png')
item2 = driver.find_element(By.CSS_SELECTOR , '#srp-river-results > ul > li:nth-child(3) > div > div.s-item__image-section > div > a > div > img')
item2.click()

list_of_handles = driver.window_handles
for handle in list_of_handles :
    if handle not in list_of_known_handles:
        new_handle = handle
        list_of_known_handles.append(new_handle)
        break
driver.switch_to.window(new_handle)
print(driver.title)

def test_1():
    assert 1==2
time.sleep(2)
driver.quit()