from django.test import TestCase
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
# Test 3.0
def test_blog_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    assert 'Blog' == driver.title

    driver.close()


# Test 3.1
def test_click_blog():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href='/blog/']").click()
    assert 'Blog' == driver.title

    driver.close()


# Test 6.0
def test_blog_CCA_details_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/8/")
    assert 'ICT Society' == driver.title

    driver.close()


# Test 6.1
def test_blog_CCA_details_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href='/blog/8/']").click()
    assert 'ICT Society' == driver.title

    driver.close()


# Test 7.0
def test_hobby_details_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/5/")
    assert 'Listening to Music' == driver.title

    driver.close()


# Test 7.1
def test_blog_hobby_details_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_xpath("//a[@href='/blog/5/']").click()
    assert 'Listening to Music' == driver.title

    driver.close()


# Test 8.0
def test_CCA_category_posts_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/CCA%20Activity/")
    assert 'Cca Activity' == driver.title

    driver.close()


# Test 8.1
def test_hobby_category_posts_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/Hobby/")
    assert 'Hobby' == driver.title

    driver.close()


# Test 8.2
def test_CCA_category_posts_click_cat():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("CCA Activity").click()
    assert 'Cca Activity' == driver.title

    driver.close()


# Test 8.3
def test_hobby_category_posts_click_cat():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Hobby").click()
    assert 'Hobby' == driver.title

    driver.close()

# Test 9.0
def test_blog_post_comments_success():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/7/")
    driver.find_element_by_name('author').send_keys('Test')
    driver.find_element_by_name('body').send_keys('Cool')
    driver.find_element_by_name("submitBtn").click()
    author = driver.find_element_by_name("authorComment").text
    body = driver.find_element_by_name("bodyComment").text
    assert 'Japanese Tsubasa Club' == driver.title
    assert author == "Test"
    assert body == "Cool"

    driver.close()

# Test 8.3
def test_hobby_category_posts_click_cat():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Hobby").click()
    assert 'Hobby' == driver.title

    driver.close()

# Test 9.0
def test_blog_post_comments_success():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/7/")
    driver.find_element_by_name('author').send_keys('Test')
    driver.find_element_by_name('body').send_keys('Cool')
    driver.find_element_by_name("submitBtn").click()
    author = driver.find_element_by_name("authorComment").text
    body = driver.find_element_by_name("bodyComment").text
    assert 'Japanese Tsubasa Club' == driver.title
    assert author == "Test"
    assert body == "Cool"

    driver.close()


# Test 9.1
def test_blog_post_comments_incomplete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/6/")
    driver.find_element_by_name('author').send_keys('Test')
    driver.find_element_by_name("submitBtn").click()
    author = driver.find_element_by_name("authorComment").text
    body = driver.find_element_by_name("bodyComment").text
    assert 'Shitoryu Karate & Ju-jitsu' == driver.title
    assert author == ""
    assert body == ""

    driver.close()


# Test 9.2
def test_blog_post_comments_maxlength():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/blog/6/")
    driver.find_element_by_name('author').send_keys('t' * 61)
    driver.find_element_by_name('body').send_keys('Cool')
    driver.find_element_by_name("submitBtn").click()
    author = driver.find_element_by_name("authorComment").text
    body = driver.find_element_by_name("bodyComment").text
    assert 'Shitoryu Karate & Ju-jitsu' == driver.title
    # Only 60 't's present
    assert author == "tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"
    assert body == "cool"

    driver.close()

