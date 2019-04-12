from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import argparse
import getpass
import p
import os

# make a new webdriver instance
driver = webdriver.Chrome()

parser = argparse.ArgumentParser(description="extending a reservation")
parser.add_argument("number", help="reservation number", default="")

argument = parser.parse_args()
status = False

no = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/show"

# open a website
driver.get(no)
driver.maximize_window()

# login to the site
login = driver.find_element_by_name("username")

username = getpass.getuser()  # gets your username from env variable LOGNAME or USER
login.send_keys(username)
login = driver.find_element_by_name("password")

# password = getpass.getpass()  # asks user for a password
# login.send_keys(p.password)  # gets password from imported pyc module
login.send_keys(os.getenv("PASS", ''))  # gets password from custom env variable PASS
time.sleep(5)
submit = driver.find_element_by_xpath("//input[@id='id_login_btn']").click()

# find duration of the testline
t = driver.find_element_by_xpath("//div[@id='duration_chosen']")

# initiate ActionChains to click and expand an option list
action_chains = ActionChains(driver)
action_chains.move_to_element(t)
action_chains.click(t)
time.sleep(2)
action_chains.perform()
time.sleep(2)

# choose option '2h' from a list
hours = driver.find_element_by_xpath("//div[@class='chosen-drop']/ul[@class='chosen-results']")
action_chains.move_to_element(hours)
time.sleep(2)
action_chains.click(hours)
time.sleep(2)
action_chains.perform()

time.sleep(5)

# hit the extend button
extend = driver.find_element_by_xpath("//input[@id='extend-button']")
extend.click()

# closes a webbrowser window
# driver.close()

