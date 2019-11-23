import pytest
import os
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_home_url_PASS():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/home")
    assert  'Home' == driver.title
    driver.close()
	
def test_check_resume_in_home_PASS():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/home")
    msg = driver.find_element_by_class_name("resume").text
    assert 'Resume' == msg
    driver.close()

def test_check_selfintro_in_home_PASS():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/home")
    msg = driver.find_element_by_class_name("selfintro").text
    assert 'Self Introduction' == msg
    driver.close()



