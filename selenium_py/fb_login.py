from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
# Navigate to the application home page
driver.get("http://www.facebook.com")

driver.find_element_by_name("email").send_keys("gskarthi@gmail.com")
driver.find_element_by_name("pass").send_keys("gfudfj")
driver.find_element_by_id("loginbutton").click()
print "Try to login"
