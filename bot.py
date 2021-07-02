###################################
#                                 #
#   Roblox Account Creation Bot   #
#         With Selenium           #
#                                 #
###################################


# Import Libaries #
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome #
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Send Get Request To Roblox #
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://roblox.com")

# Enter DoB #
search = driver.find_element_by_id("MonthDropdown").click()
driver.find_element_by_xpath("//Option[@value='Jun']").click()

search = driver.find_element_by_id("DayDropdown").click()
driver.find_element_by_xpath('//Option[@value="09"]').click()

search = driver.find_element_by_id("YearDropdown").click()
driver.find_element_by_xpath('//Option[@value="1969"]').click()

# Type In Username #
search = driver.find_element_by_id("signup-username")
search.send_keys("ChangeUsername")

# Type In Password #
search = driver.find_element_by_id("signup-password")
search.send_keys("ChangePassword")

# Select Player Gender #
search = driver.find_element_by_id("MaleButton").click()

# Enter Credentials #
search = driver.find_element_by_id("signup-button").click()
