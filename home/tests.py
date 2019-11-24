from django.test import TestCase
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
# Test 2.0
def test_home_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/home")
    assert 'Portfolio' == driver.title

    driver.close()


# Test 2.1
def test_home_click_portfolio():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/home")
    driver.find_element_by_xpath("//a[@href='/home/']").click()
    assert 'Portfolio' == driver.title

    driver.close()


# Test 2.2
def test_home_click_link():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/home")
    driver.find_element_by_xpath("//a[@href='/home/']").click()
    assert 'Portfolio' == driver.title

    driver.close()

