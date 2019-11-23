import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_access_blog():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/")
    assert  'Blog' == driver.title
    driver.close()

def test_access_blog_categories_projects():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/Projects/")
    chkmsg = driver.find_element_by_xpath("//div/h1").text
    assert  'Blog Categories' == driver.title and "Projects" == chkmsg
    driver.close()

def test_access_blog_post_from_blog_by_clicking():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/Projects/")
    driver.find_element_by_xpath("//a[@href='/blog/4/' and text()='First android project']").click()
    chkmsg = driver.find_element_by_xpath("//div/h1").text
    assert  'http://127.0.0.1:8000/blog/4/' == driver.current_url and "First android project" == chkmsg
    driver.close()

def test_blog_post_comment_form_hidden():
    cmtform = ""
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/4/")
    try :
        element= driver.find_element_by_xpath("//form")
        if element.is_displayed():
            cmtform == "there"
            return(cmtform)
        else:
            cmtform == "not there"
            return(cmtform)
    except:
        cmtform == "not there"
        return(cmtform)
    assert 'not there' == cmtform
    driver.close()

def test_blog_post_comment_form_shown():
    cmtform = ""
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(4)
    driver.get("http://127.0.0.1:8000/blog/4/")
    try :
        element= driver.find_element_by_xpath("//form")
        if element.is_displayed():
            cmtform == "there"
            return(cmtform)
        else:
            cmtform == "not there"
            return(cmtform)
    except:
        cmtform == "not there"
        return(testing)
    assert 'there' == cmtform
    driver.close()

def test_blog_post_empty_comment():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(4)
    driver.get("http://127.0.0.1:8000/blog/4/")
    countNoOfComment = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_xpath("//button[@type='submit' and text()='Submit']").submit()
    countNoOfCommentAfterClick = len(driver.find_elements_by_name('usercomment'))
    assert countNoOfComment == countNoOfCommentAfterClick
    driver.close()

def test_blog_post_author_empty():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(4)
    driver.get("http://127.0.0.1:8000/blog/4/")
    countNoOfComment = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("body").send_keys("testing")
    driver.find_element_by_xpath("//button[@type='submit' and text()='Submit']").submit()
    countNoOfCommentAfterClick = len(driver.find_elements_by_name('usercomment'))
    assert countNoOfComment == countNoOfCommentAfterClick
    driver.close()

def test_blog_post_body_empty():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(4)
    driver.get("http://127.0.0.1:8000/blog/4/")
    countNoOfComment = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("author").send_keys("jiawei")
    driver.find_element_by_xpath("//button[@type='submit' and text()='Submit']").submit()
    countNoOfCommentAfterClick = len(driver.find_elements_by_name('usercomment'))
    assert countNoOfComment == countNoOfCommentAfterClick
    driver.close()

def test_blog_post_valid_comment():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    time.sleep(4)
    driver.get("http://127.0.0.1:8000/blog/4/")
    countNoOfComment = len(driver.find_elements_by_name('usercomment'))
    driver.find_element_by_name("author").send_keys("Chua Jiawei")
    driver.find_element_by_name("body").send_keys("Fantastic")
    driver.find_element_by_xpath("//button[@type='submit' and text()='Submit']").submit()
    countNoOfCommentAfterClick = len(driver.find_elements_by_name('usercomment'))
    assert (countNoOfCommentAfterClick == countNoOfComment +1)
    driver.close()




