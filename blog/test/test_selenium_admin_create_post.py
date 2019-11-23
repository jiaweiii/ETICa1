import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_create_blog_post_empty_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/post/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the errors below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add post | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_blog_post_empty_body_categories():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/post/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the errors below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add post | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_blog_post_empty_categories():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/post/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Test")
    driver.find_element_by_name("body").send_keys("Test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add post | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_blog_post_empty_title():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/post/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Test")
    catselection = driver.find_element_by_xpath("//select/option[@value='1']")
    catselection.click()
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add post | Jw Portfolio Portal' == driver.title
    driver.close()

def test_admin_add_unique_blog_post():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/blog/post/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    driver.find_element_by_xpath("//a[@class='addlink']").click()
    time.sleep(3)
    driver.find_element_by_name("title").send_keys("Track & Field")
    driver.find_element_by_name("body").send_keys("I did ....")
    catselection = driver.find_element_by_xpath("//select/option[@value='1']")
    catselection.click()
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    time.sleep(3)
    row_count2 = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    assert (row_count2 == row_count +1 and 'Select post to change | Jw Portfolio Portal' == driver.title)
    driver.close()

