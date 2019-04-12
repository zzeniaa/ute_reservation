from selenium import webdriver
import time
import argparse
import getpass
import p
import os

# make a new webdriver instance
driver = webdriver.Chrome()

parser = argparse.ArgumentParser(description="extending a reservation")
parser.add_argument("number", help="reservation number", default="")
parser.add_argument("--time", "-t", help="duration [hours]: 1, 2 or 3", default="")

argument = parser.parse_args()
status = False

if argument.time == '2':
    extend_2h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/120"
    driver.get(extend_2h)
    status = True
if argument.time == '3':
    extend_3h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/180"
    driver.get(extend_3h)
    status = True
else:
    extend_1h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/60"
    driver.get(extend_1h)

driver.maximize_window()

# login to the site
login = driver.find_element_by_name("username")

username = getpass.getuser()  # gets your username from env variable LOGNAME or USER
login.send_keys(username)
login = driver.find_element_by_name("password")

# password = getpass.getpass()  # asks user for a password
login.send_keys(p.password)  # gets password from imported pyc module
# login.send_keys(os.getenv("PASS", ''))  # gets password from custom env variable PASS
time.sleep(2)
submit = driver.find_element_by_xpath("//input[@id='id_login_btn']").click()

# closes a webbrowser window
time.sleep(3)
driver.close()

