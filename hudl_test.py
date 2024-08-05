# Description: This file contains the test cases for the hudl application.
import pytest
import pytest_html
from selenium import webdriver
from hudl_page_objects import LoginPage, HomePage
from variables import *

@pytest.fixture
# Setting up driver with chrome in headless mode
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

# verify login to hudl using valid credentials & verify team name
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login_to_hudl(hudl_url, hudl_username, hudl_password)
    home_page = HomePage(driver)
    home_page.verify_successful_login()
    home_page.verify_team_name(team_name)

# verify search placeholder before and after click & verify search results is not empty with valid a string for eg. John
def test_search_with__string(driver):
    login_page = LoginPage(driver)
    login_page.login_to_hudl(hudl_url, hudl_username, hudl_password)
    home_page = HomePage(driver)
    home_page.verify_successful_login()
    home_page.watch_now()
    home_page.search()
    actual_result_list = home_page.verify_search_results(search_string_with_valid_char)
    print("Total no of search results - {}".format(actual_result_list))
    assert actual_result_list > 1, "Result list is empty - {}".format(actual_result_list)

# verify search results is empty with a string containing special characters for eg. !@#$%^&^@#!@$%^&@
def test_search_with_random_string(driver):
    login_page = LoginPage(driver)
    login_page.login_to_hudl(hudl_url, hudl_username, hudl_password)
    home_page = HomePage(driver)
    home_page.verify_successful_login()
    home_page.watch_now()
    home_page.search()
    actual_result_list = home_page.verify_search_results(search_string_with_junk_char)
    assert actual_result_list == 0, "Result list is not empty - {}".format(actual_result_list)
