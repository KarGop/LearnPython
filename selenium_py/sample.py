from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
# Navigate to the application home page
driver.get("http://www.python.org")
# to confirm that title has "Python" word in it
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
print elem
elem.clear()
elem.send_keys("karthika")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
