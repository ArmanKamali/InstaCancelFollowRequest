

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


driver = webdriver.Chrome(executable_path=r'D:\\Programming\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.find_element_by_name('username').send_keys()