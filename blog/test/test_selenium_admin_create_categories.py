import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_add_blog_category_empty_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/category/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add category | Jw Portfolio Portal' == driver.title
    driver.close()

def test_add_unique_blog_category():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/admin/blog/category/' and text()='Categorys']").click()
    time.sleep(3)
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    driver.find_element_by_xpath("//a[@class='addlink']").click()
    time.sleep(3)
    driver.find_element_by_name("name").send_keys("CCA")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    time.sleep(1)
    row_count2 = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    assert row_count2 == row_count +1 and 'Select category to change | Jw Portfolio Portal' == driver.title
    driver.close()





