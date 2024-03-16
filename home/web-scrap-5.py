from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
driver = webdriver.Chrome()
login_url = "https://winwins.app/#/login"
win_url = "https://winwins.app/#/win"

# Navigate to the login page
driver.get(login_url)

# Find username and password fields, and login button
# username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
# password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
# login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]")))

# Fill in username and password, then click login button
# username_field.send_keys("7820867566")
# password_field.send_keys("@Akshay93")
# login_button.click()

username_field = driver.find_element(By.XPATH, "//input[@type='text']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")

username_field.send_keys("7820867566")
password_field.send_keys("@Akshay93")

print('Adding credintionals')

login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_button.click()
print('login succesfull')

# Wait for the redirect to the win page
# WebDriverWait(driver, 10).until(EC.url_to_be(win_url))
driver.get(win_url)

# Get the HTML content after JavaScript has been executed
# html = driver.page_source

# Use BeautifulSoup to parse the HTML
# soup = BeautifulSoup(html, 'html.parser')

# Find the table element
# table = soup.find('table')

# if table is not None:
#     # Get all rows in the table
#     rows = table.find_all('tr')

#     # Print the content of each cell in each row
#     for row in rows:
#         cells = row.find_all('td')
#         for cell in cells:
#             print(cell.text.strip())
# else:
#     print("Table not found")
# Close the browser when done




wait = WebDriverWait(driver, 10)
table = wait.until(driver.find_element(By.XPATH, "//[@type='password']"))
# Get the HTML content of the table
table_html = table.get_attribute('outerHTML')

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(table_html, 'html.parser')

# Extract data from the table as needed
# For example, find all rows and cells
rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.text.strip())

driver.quit()