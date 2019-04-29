from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse
import getpass
import p
import os

parser = argparse.ArgumentParser(description="creating a single run")
parser.add_argument("-tl", "--testline", help="testline type", required=False, default="CLOUD_R4P")
parser.add_argument("directory", help="directory", default="")
parser.add_argument("test", help="test suite name", default="")
parser.add_argument("-s", "--state", help="eNB state", default="configured")
parser.add_argument("-e", "--enb", help="eNB build; default is latest FSMr4 build on trunk", default="FL00_FSM4")
parser.add_argument("-u", "--ute", help="UTE build; default is the latest one", default="")
parser.add_argument("-r", "--repo", help="test repository revision", required=False, default="HEAD")

argument = parser.parse_args()

# make a new webdriver instance
driver = webdriver.Chrome()
driver.get("https://cloud.ute.inside.nsn.com/execution/create")
driver.maximize_window()

# login to the site
login = driver.find_element_by_name("username")

login.send_keys(getpass.getuser())  # gets your username from env variable LOGNAME or USER
login = driver.find_element_by_name("password")
login.send_keys(p.password)  # gets password from imported pyc module
submit = driver.find_element_by_xpath("//input[@id='id_login_btn']").click()

test_path = driver.find_element_by_name("test_path")
path = "testsuite/WMP/DevWro1L2/LTE/" + argument.directory + "/" + argument.test
test_path.send_keys((Keys.CONTROL, "a"))
test_path.send_keys(path)

tl = driver.find_element_by_name("testline_type")
arrow = driver.find_element_by_id("mat-select-0").click()
tl_field = driver.find_element_by_id("mat-input-4")
tl_field.send_keys(argument.testline)
time.sleep(2)
tl_field.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

enb_state = driver.find_element_by_id("mat-select-1").click()
time.sleep(2)

if argument.state == 'enb_configured':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[5]").click()

if argument.state == 'configured':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[6]").click()

if argument.state == 'commissioned':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[4]").click()

if argument.state == 'ssh_only':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[1]").click()

if argument.state == 'enb_initializing':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[2]").click()

if argument.state == 'enb_commissioned':
    enb = driver.find_element_by_xpath("//div[@class='cdk-overlay-container']/div/div/div/div/mat-option[3]").click()

if argument.ute:
    ute_build = driver.find_element_by_id("mat-select-5")
    ute_build.send_keys((Keys.CONTROL, "a"))
    ute_build.send_keys(argument.ute)

test_revision = driver.find_element_by_id("mat-input-1")
test_revision.send_keys(Keys.CONTROL, "a")
test_revision.send_keys(argument.repo)

arrow = driver.find_element_by_id("mat-select-3").click()
enb_build = driver.find_element_by_id("mat-input-6")
enb_build.send_keys(argument.enb)
time.sleep(2)
enb_build.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

time.sleep(2)
# Click on "Create" button
driver.find_element_by_xpath("//*[(text()='Create')]").click()
