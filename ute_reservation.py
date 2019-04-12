from selenium import webdriver
import time
import argparse
import getpass
import p
import os

parser = argparse.ArgumentParser(description="extending a reservation")
parser.add_argument("number", help="reservation number", default="")
parser.add_argument("--time", "-t", help="duration [hours]: 1, 2 or 3", default="")

argument = parser.parse_args()

if argument.time == '2':
    extend_2h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/120"
    driver.get(extend_2h)
    
if argument.time == '3':
    extend_3h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/180"
    driver.get(extend_3h)
    
if argument.time == '1':
    extend_1h = "https://cloud.ute.inside.nsn.com/reservation/" + argument.number + "/extend/60"
    driver.get(extend_1h)

else:
    print("invalid value! choose from: [1,2,3]")
    exit()

# make a new webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# login to the site
login = driver.find_element_by_name("username")

login.send_keys(getpass.getuser())  # gets your username from env variable LOGNAME or USER
login = driver.find_element_by_name("password")

# password = getpass.getpass()  # asks user for a password
login.send_keys(p.password)  # gets password from imported pyc module
# login.send_keys(os.getenv("PASS", ''))  # gets password from custom env variable PASS
time.sleep(2)
submit = driver.find_element_by_xpath("//input[@id='id_login_btn']").click()

# closes a webbrowser window
time.sleep(3)
driver.close()

