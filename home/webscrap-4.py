from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
# from config import user,password

# Set up Selenium WebDriver
driver = webdriver.Chrome()
url_login = "https://winwins.app/#/login"
url_data = "https://winwins.app/#/win"

# Navigate to the login page
driver.get(url_login)

# Wait for the page to load (you may need to adjust the wait time)
time.sleep(3)  # Adjust the sleep time as needed

# Find the username and password input fields using XPath
username_field = driver.find_element(By.XPATH, "//input[@type='text']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

username_field.send_keys("7820867566")
password_field.send_keys("@Akshay93")

print('Adding credintionals')


# Find and click the login button
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_button.click()
print('login succesfull')

# Wait for the login process to complete (you may need to adjust the wait time)
time.sleep(3)  # Adjust the sleep time as needed

# Navigate to the data page
# driver.get(url_data)
driver.get(url_data)


# Wait for the data page to load (you may need to adjust the wait time)
# time.sleep(5)  # Adjust the sleep time as needed

# Get the HTML content of the data page
# html = driver.page_source



html = driver.page_source

time.sleep(5)

# table = pd.read_html(url_data)
# print(table)
# print('check-content')

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# tbody = soup.find('div', class_='parity')
# # print(soup.prettify())
# print(tbody)

trs = soup.find_all('tr')

# Iterate over each <tr> element and find all <td> elements within it
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td)

print('getting data')

time.sleep(10)

# Don't forget to close the browser when done

driver.quit()



