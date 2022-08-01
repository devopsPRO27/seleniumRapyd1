import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class GooglePage:
    def __init__(self,driver):
        self.driver=driver
        self.driver.get('https://www.google.com')

    def search(self,text):
        search_TB = self.driver.find_element(By.NAME , 'q')
        search_TB.clear()
        search_TB.send_keys(text)
        search_btn= self.driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')
        search_btn.click()
        print("search done")

    def click_on_link(self):
        imdblink=self.driver.find_element(By.CSS_SELECTOR,'#rso > div:nth-child(1) > div > div > div > div > div > div.yuRUbf > a > h3')
        imdblink.click()
        print('click on link done ')

class IMDBPage:
    def __init__(self,driver):
        self.driver = driver
        #if self.driver.current_url()[7:11] == 'imdb':

    def heading_text(self):
        h1=self.driver.find_element(By.CSS_SELECTOR,'#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-c7f03a63-0.kUbSjY > section > div:nth-child(4) > section > section > div.sc-94726ce4-0.cMYixt > div.sc-94726ce4-2.khmuXj > h1')
        return h1.text





