from django.test import TestCase
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Create your tests here.
# Test 1.0.0
def test_admin_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    assert 'Log in | Django site admin' == driver.title
    
    driver.close()


# Test 1.0.1
def test_admin_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    assert 'Site administration | Django site admin' == driver.title
    
    driver.close()


# Test 1.0.2
def test_admin_invalid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("testing")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    error = driver.find_element_by_class_name("errornote").text
    assert 'Log in | Django site admin' == driver.title
    assert 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.' == error
    
    driver.close()


# Test 1.0.3
def test_admin_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    a = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[3]")
    time.sleep(1)
    a.click()
    assert 'Logged out | Django site admin' == driver.title
    
    driver.close()


# Test 1.1.0 
def test_admin_new_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/auth/user/")
    counter = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert 'Add user | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("testingtesting")
    driver.find_element_by_name("password1").send_keys("passwordhello")
    driver.find_element_by_name("password2").send_keys("passwordhello")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Change user | Django site admin' == driver.title
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert 'Select user to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr"))
    assert counter2 - counter == 1
    driver.close() 


# Test 1.1.1
def test_admin_new_user_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/auth/user/")
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert  'Add user | Django site admin' == driver.title
    driver.find_element_by_name("username").send_keys("testingtesting")
    driver.find_element_by_name("password1").send_keys("password")
    driver.find_element_by_name("password2").send_keys("testing")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert 'Add user | Django site admin' == driver.title
    error = driver.find_element_by_class_name("errorlist").text
    assert "The two password fields didn't match." == error
    driver.close()


# Test 1.1.2
def test_admin_new_user_maxlength():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/auth/user/")
    counter = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert 'Add user | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("t" * 151)
    driver.find_element_by_name("password1").send_keys("testingtest123")
    driver.find_element_by_name("password2").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Change user | Django site admin' == driver.title
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert 'Select user to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr"))
    assert counter2 - counter == 1
    driver.close() 


# Test 1.2.0
def test_admin_new_category():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/blog/category/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert 'Add category | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("testing")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select category to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.2.1
def test_admin_new_category_maxlength():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/blog/category/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert 'Add category | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("t" * 21)
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select category to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.3.0
def test_admin_new_post():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/blog/post/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert  'Add post | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("title").send_keys("testing")
    driver.find_element_by_name("body").send_keys("testing")
    driver.find_element_by_xpath("//*[@id=\"id_categories\"]/option[1]").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select post to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.3.1
def test_admin_new_post_maxlength():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/blog/post/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert  'Add post | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("title").send_keys("t" * 256)
    driver.find_element_by_name("body").send_keys("testing")
    driver.find_element_by_xpath("//*[@id=\"id_categories\"]/option[1]").click()
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select post to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.4.0
def test_admin_new_group():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/auth/group/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert  'Add group | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("testing")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select group to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.4.1
def test_admin_new_group_maxlength():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    time.sleep(1)
    driver.get("http://localhost:8000/admin/auth/group/")
    counter = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
    assert  'Add group | Django site admin' == driver.title
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("t" * 151)
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Save']").click()
    assert  'Select group to change | Django site admin' == driver.title
    counter2 = len(driver.find_elements_by_xpath("//*[@id=\"result_list\"]/tbody/tr"))
    assert counter2 - counter == 1
    driver.close()


# Test 1.5.0
def test_admin_change_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    a = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[2]")
    time.sleep(1)
    a.click()
    assert 'Password change' == driver.title
    time.sleep(1)
    driver.find_element_by_id("id_old_password").send_keys("testingtest123")
    driver.find_element_by_name("new_password1").send_keys("testest1234")
    driver.find_element_by_name("new_password2").send_keys("testest1234")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Change my password']").click()
    assert 'Password change successful' == driver.title

    driver.close()


# Test 1.5.1
def test_admin_change_password_different_pw():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    a = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[2]")
    time.sleep(1)
    a.click()
    assert 'Password change' == driver.title
    time.sleep(1)
    driver.find_element_by_id("id_old_password").send_keys("testingtest123")
    driver.find_element_by_name("new_password1").send_keys("testest1234")
    driver.find_element_by_name("new_password2").send_keys("testest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Change my password']").click()
    error = driver.find_element_by_class_name("errorlist").text
    assert "The two password fields didn't match." == error

    driver.close()


# Test 1.5.2
def test_admin_change_password_wrong_pw():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    a = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[2]")
    time.sleep(1)
    a.click()
    assert 'Password change' == driver.title
    time.sleep(1)
    driver.find_element_by_id("id_old_password").send_keys("wrongpassword")
    driver.find_element_by_name("new_password1").send_keys("testest123")
    driver.find_element_by_name("new_password2").send_keys("testest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Change my password']").click()
    error = driver.find_element_by_class_name("errorlist").text
    assert "Your old password was entered incorrectly. Please enter it again." == error

    driver.close()


# Test 1.5.3
def test_admin_change_password_insufficient_chara():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("nh")
    driver.find_element_by_name("password").send_keys("testingtest123")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Log in']").click()
    a = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[2]")
    time.sleep(1)
    a.click()
    assert 'Password change' == driver.title
    time.sleep(1)
    driver.find_element_by_id("id_old_password").send_keys("testingtest123")
    driver.find_element_by_name("new_password1").send_keys("@#$%")
    driver.find_element_by_name("new_password2").send_keys("@#$%")
    driver.find_element_by_xpath("//input[@type = 'submit' and @value='Change my password']").click()
    error = driver.find_element_by_class_name("errorlist").text
    assert "This password is too short. It must contain at least 8 characters." == error

    driver.close()


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