from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/hothaifa/Desktop/chromedriver')


driver.get('https://demo.automationtesting.in/Register.html')

first_name = driver.find_element('css selector' , value= '#basicBootstrapForm > div:nth-child(1) > div:nth-child(2) > input')
first_name .send_keys('hodi')

driver.find_element('css selector',
                    '#basicBootstrapForm > div:nth-child(7) > div > multi-select').click()
language = driver.find_element('css selector' ,
                               '#basicBootstrapForm > div:nth-child(7) > div > multi-select > div:nth-child(2) > ul > li:nth-child(1)')

language.click()