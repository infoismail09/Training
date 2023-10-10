from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:/Users/Nimap/OneDrive/Documents/NImap_Internship/selenium_project_practice/chromedriver.exe")
# driver.get('https://www.google.com/')
# driver.maximize_window()
# time.sleep(2)

# GoogleSearchBox = driver.find_element_by_id('APjFqb')
# GoogleSearchBox.send_keys("Automation")
# # serchBox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
# # serchBox.click()
# # OR
# GoogleSearchBox.send_keys(Keys.RETURN)  # this functionality is like you press enter after typing siomething



driver.get('https://trytestingthis.netlify.app/')
driver.find_element_by_id('fname').send_keys('Dhinchak')
driver.find_element_by_id('lname').send_keys('Pandya')
time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/fieldset/button') this is relative x path
Submit_button = driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
time.sleep(2)





