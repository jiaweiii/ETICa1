import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_create_user_empty_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password1").send_keys("")
    driver.find_element_by_name("password2").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    time.sleep(1)
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the errors below.' == ermsg1 and 'This field is required.' == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_existing_username_empty_password_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password1").send_keys("")
    driver.find_element_by_name("password2").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'A user with that username already exists.')]").text
    ermsg3 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the errors below.' == ermsg1 and 'A user with that username already exists.' == ermsg2 and 'This field is required.' == ermsg3 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_password_similar_to_username():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("jiawei")
    driver.find_element_by_name("password1").send_keys("jiawei123")
    driver.find_element_by_name("password2").send_keys("jiawei123")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'The password is too similar to the username.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'The password is too similar to the username.' == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()  

def test_create_user_password_less_than_8_characters():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("jiawei")
    driver.find_element_by_name("password1").send_keys("passwor")
    driver.find_element_by_name("password2").send_keys("passwor")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This password is too short. It must contain at least 8 characters.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'This password is too short. It must contain at least 8 characters.' == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_password_is_numeric():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("jiawei")
    driver.find_element_by_name("password1").send_keys("123456789")
    driver.find_element_by_name("password2").send_keys("123456789")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This password is entirely numeric.')]").text
    assert 'Please correct the error below.' == ermsg1 and 'This password is entirely numeric.' == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_password_is_different_from_confirm_password():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("newtest")
    driver.find_element_by_name("password1").send_keys("Str0ngP@ww0rd")
    driver.find_element_by_name("password2").send_keys("Str0ngP@ww0rd123")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_class_name("errorlist")
    ermsg3 = ermsg2.find_element_by_tag_name("li").text
    assert 'Please correct the error below.' == ermsg1 and "The two password fields didn't match." == ermsg3 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_username_empty():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password1").send_keys("Str0ngP@ww0rd")
    driver.find_element_by_name("password2").send_keys("Str0ngP@ww0rd")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the error below.' == ermsg1 and "This field is required." == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_user_confirmpassword_empty():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    driver.find_element_by_name("username").send_keys("testing1997")
    driver.find_element_by_name("password1").send_keys("Str0ngP@ww0rd")
    driver.find_element_by_name("password2").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    ermsg1 = driver.find_element_by_class_name("errornote").text
    ermsg2 = driver.find_element_by_xpath("//*[contains(text(), 'This field is required.')]").text
    assert 'Please correct the error below.' == ermsg1 and "This field is required." == ermsg2 and 'Add user | Jw Portfolio Portal' == driver.title
    driver.close()

def test_create_unique_user_valid_credentials():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/auth/user/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(3)
    row_count = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    driver.find_element_by_xpath("//a[@class='addlink']").click()
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("testing")
    driver.find_element_by_name("password1").send_keys("Str0nkP@ssw0rd")
    driver.find_element_by_name("password2").send_keys("Str0nkP@ssw0rd")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Save']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[@href='/admin/auth/user/' and text()='Users']").click()
    row_count2 = len(driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    assert row_count2 == row_count +1
    driver.close()

