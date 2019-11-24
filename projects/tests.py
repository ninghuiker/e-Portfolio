from django.test import TestCase
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
# Test 4.0
def test_blog_project_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/")
    assert 'Projects' == driver.title

    driver.close()

# Test 4.1
def test_blog_project_click_btn():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_name("projectBtn").click()
    assert 'Projects' == driver.title

    driver.close()


# Test 5.0
def test_blog_project_details_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/8/")
    assert 'Brave (GPP)' == driver.title

    driver.close()


# Test 5.1
def test_blog_project_details_click_more():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/projects/")
    driver.find_element_by_name("readMore").click()
    assert 'Brave (GPP)' == driver.title

    driver.close()