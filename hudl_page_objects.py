# Description: This file contains page objects for login page & home page of hudl application
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables import *
import time

class LoginPage:
    # initialize login page with below objects
    def __init__(self, driver):
        self.driver = driver
        self.login_option = (By.XPATH, "//a[@data-qa-id='login-select']")    #login button
        self.login_hudl_btn = (By.XPATH, "//a[@data-qa-id='login-hudl']")    #hudl button
        self.email = (By.ID, "email")      #email textbox
        self.password = (By.ID, "password")     #password textbox
        self.continue_login_btn = (By.ID, "logIn")      #button to enter login

    # open the webpage with specified url
    def open_page(self, url):
        self.driver.get(url)

    # open login page of hudl by clicking on login button & then hudl button
    def open_login_page(self):
        self.driver.find_element(*self.login_option).click()
        self.driver.find_element(*self.login_hudl_btn).click()
        
    # enter username in email textbox
    def enter_username(self, username):
        self.driver.find_element(*self.email).send_keys(username)

    # enter password in password textbox
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    # click on continue button to login
    def click_continue(self):
        self.driver.find_element(*self.continue_login_btn).click()

    # login to hudl using url, username & password
    def login_to_hudl(self, url, username, password):
        self.driver.get(url)
        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_continue()

class HomePage:
    # initialize home page with below objects
    def __init__(self, driver):
        self.driver = driver
        self.home_page = (By.ID, "home-content")    #home page
        self.team_name_object = (By.CLASS_NAME, "hui-primaryteamswitcher__display-name")    # web object that contains team name
        self.upload_video_btn = (By.XPATH, "//a[@data-qa-id='webnav-globalnav-upload']")    #upload video button
        self.notification_link = (By.ID, "notifications-link")    #notification link
        self.messages_link = (By.XPATH, "//a[@data-qa-id='webnav-globalnav-messages']")    #messages link
        self.watch_now_menu_option = (By.XPATH, "//a[@data-qa-id='webnav-globalnav-watchnow']")     #watch now menu option
        self.fan_home_page = (By.XPATH, '//div[@data-qa-id="fan-home-page"]')      #fan home page
        self.search_input_textbox = (By.ID, "uniId_:r0:")       #search input textbox
        self.search_results = (By.XPATH, "//li[@data-qa-id='search-results-group']/li[@class='styles_optionContainer__QepZb']")    #list of search results after typing some string in search box
        self.empty_list_container = (By.XPATH, "//div[@data-qa-id='search-empty-state-container']")     # empty list when no results are found

    def verify_successful_login(self):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.home_page))
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.upload_video_btn))
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.notification_link))
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.messages_link))
            print("Login successful")
        except:
            print("Either home page not loaded or login failed. Kindly check the login credentials")
            exit()
    # verify team name on home page
    def verify_team_name(self, team_name):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.home_page))
            print(self.driver.find_element(*self.team_name_object).get_attribute("innerText"))
            assert self.driver.find_element(*self.team_name_object).get_attribute("innerText") == team_name, "Actual team name - {} not matching expected team name - {}".format(self.driver.find_element(*self.team_name_object).get_attribute("innerText"), team_name)
        except:
            print("Either home page not loaded or login failed. Kindly check the login credentials")
            exit()
            
    # click on watch now menu option to navigate to fan home page
    def watch_now(self):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.home_page))
            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(self.watch_now_menu_option))
            self.driver.find_element(*self.watch_now_menu_option).click()
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(self.fan_home_page))
        except Exception as e:
            print("Either home page not loaded or login failed. Kindly check the login credentials")
            exit(e)


    # click on search box & verify the placeholder text before & after click changes
    def search(self):
        try:
            x = WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(self.search_input_textbox))
            placeholder_text_before_click = self.driver.find_element(*self.search_input_textbox).get_attribute("placeholder")
            assert placeholder_text_before_click == expected_search_placeholder_before_click, "Search placeholder string mismtach - Actual: {}, Expected: {}".format(placeholder_text_before_click, expected_search_placeholder_before_click)
            self.driver.find_element(*self.search_input_textbox).click()
            placeholder_text_after_click = self.driver.find_element(*self.search_input_textbox).get_attribute("placeholder")
            # Below line is commented because in visual mode the string is different & in headless mode it is different
            # assert placeholder_text_after_click == expected_search_placeholder_after_click, "Search placeholder string mismtach - Actual: {}, Expected: {}".format(placeholder_text_after_click, expected_search_placeholder_after_click)
        except:
            print("Search option not loaded or available")
            exit()
        
    # verify search results are not empty with valid search string & empty when search string contains special characters (no results found)    
    def verify_search_results(self, search_text):
        self.driver.find_element(*self.search_input_textbox).send_keys(search_text)
        try:
            result_list = WebDriverWait(self.driver, delay).until(EC.presence_of_all_elements_located (self.search_results))
        except:
            self.driver.find_element(*self.empty_list_container).is_displayed()
            result_list = []
        finally:
            return len(result_list)