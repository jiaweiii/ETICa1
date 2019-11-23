import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_view_list_of_registered_users():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    assert  'Select user to change | Jw Portfolio Portal' == driver.title and row_count >= 1
    driver.close()

def test_view_admin_user():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/admin/auth/user/2/change/' and text()='admin']").click()
    usernametxtbox = driver.find_element_by_name("username").get_attribute('value')
    assert  'Change user | Jw Portfolio Portal' == driver.title and 'admin' == usernametxtbox and 'http://127.0.0.1:8000/admin/auth/user/2/change/' == driver.current_url
    driver.close()

