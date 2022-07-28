import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

# Keys
path = '/Users/hothaifa/Desktop/chromedriver'
#
# driver = webdriver.Chrome(path)
#
# driver.get('https://wwww.amazon.com')  # open  the url that we gave
# # time.sleep(2)
# # print(driver.current_url)
# # print(driver.title)
# # print(driver.timeouts)
# #
# # driver.get('https://www.zara.com/')
# # time.sleep(2)
# # print(driver.current_url)
#
# driver.get('https://www.amazon.com')
# time.sleep(4)
# driver.find_element_by_xpath('//*[@id="nav-cart"]')
# time.sleep(3)
#
# driver.quit()

driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

driver.get('file:///Users/hothaifa/PycharmProjects/selenium26.07/index.html')

img_element = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR , '#the_slow_image > img')))

img_web_element=driver.find_element(By.CSS_SELECTOR,'#the_slow_image > img')
# '#the_slow_image > img')

print(img_web_element.size)
img_web_element.send_keys(Keys.ENTER)
