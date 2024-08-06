# Description: This file contains the variables that are used in the test cases.
import os
hudl_url = "https://www.hudl.com"   # hudl url

# get the username & password from environment variables, if not present throw error message & exit
if os.getenv('HUDL_USERNAME') is not None:
    hudl_username = os.getenv('HUDL_USERNAME')
else:
    print("********************   Please set HUDL_USERNAME environment variable   ********************")
    exit()

if os.getenv('HUDL_PASSWORD') is not None:
    hudl_password = os.getenv('HUDL_PASSWORD')
else:
    print("********************   Please set HUDL_PASSWORD environment variable   ********************")
    exit() 

expected_team_name = "Newcastle Jets FC"     # team name. Change this if username used belongs to another team
search_string_with_valid_char = "John"   # search string with valid characters
search_string_with_special_char = "!@#$%^&^@#!@$%^&@"  # search string with special characters
expected_search_placeholder_before_click = "Search Hudl Fan"    # expected search placeholder before click
# Below string in visual mode
expected_search_placeholder_after_click = "Search for an player, school, club, association or league"  # expected search placeholder after click
# Below string in headless mode
expected_search_placeholder_after_click_alternative = "Search for an athelete, school, club, association or league"  # expected search placeholder after click
delay = 10   # delay time for waiting for an element to be present on the page