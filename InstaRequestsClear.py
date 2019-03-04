import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup

# username and password of user
username = "atlasbentglass"
password = "0322542812"
# get driver

driver = webdriver.Firefox()
# go to login page
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
# wait until load and go to userpage
usernameInput = WebDriverWait(driver, 5).until(
    lambda x: x.find_element_by_name("username"))

passwordInput = WebDriverWait(driver, 5).until(
    lambda x: x.find_element_by_name("password"))

submitBtn = WebDriverWait(driver, 5).until(
    lambda x: x.find_element_by_xpath("//button[contains(.,'Log in')]"))
# after get all info login

usernameInput.send_keys(username)
passwordInput.send_keys(password)
submitBtn.click()
time.sleep(5)
for i in range(1, 100):
    driver.get('https://www.instagram.com/accounts/access_tool/current_follow_requests')
    try:
        viewBtn = WebDriverWait(driver, 5).until(
            lambda x: x.find_element_by_xpath("//button[contains(.,'View More')]"))
        while viewBtn:
            viewBtn.click()
            time.sleep(2)
    except:
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        people = soup.find_all('div', {'class', '-utLf'})
        print(len(people))
        for person in people:
            url = "https://instagram.com/" + person.text
            driver.get(url)
            requestBtn = WebDriverWait(driver, 5).until(
                lambda x: x.find_element_by_xpath("//button[contains(.,'Requested')]"))
            requestBtn.click()
            okBtn = WebDriverWait(driver, 5).until(
                lambda x: x.find_element_by_xpath("//button[contains(.,'Unfollow')]"))
            okBtn.click()
