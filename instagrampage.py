from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = input("your_username of insta: ")
password = input("your_password of insta: ")

driverpath= "chromedriver.exe"
service = Service(driverpath)
driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/accounts/login/")
print(driver.title)
driver.maximize_window()

time.sleep(4) 

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
time.sleep(2)
password_input.send_keys(Keys.RETURN)

time.sleep(7)  


driver.get(f"https://www.instagram.com/{username}/")
time.sleep(5)


profile_icon = driver.find_element(By.XPATH, "//img[@alt='Profile photo']")
profile_icon.click()
time.sleep(3)


logout_button = driver.find_element(By.XPATH, "//div[text()='Log Out']")
logout_button.click()

time.sleep(5)
driver.quit()
