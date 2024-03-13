from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import Request
import requests

# url = 'https://winwins.app/#/login'

driver = webdriver.Chrome()

login_url = 'https://winwins.app/#/login'
target_url = 'https://winwins.app/#/win'

payload = {
    'mobile number':'9370664563',
    'password':'@Sniper9370',
}

start = requests.post(login_url, data=payload)

driver.get(target_url)

driver.implicitly_wait(2)

# def get_page(url):
#     """Get the content of a web page."""
#     response = requests.get(url)
#     try:
#         html_content = urlopen(response).read()
#         return BeautifulSoup(html_content, "html.parser")
#     except Exception as e:
#         print("Error opening URL {}: {}".format(url, str(e)))
#         return None
    
# response = requests.get(url)
# print(response.status_code)

# response = requests.get(url)

# html_content =  response.content

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())

# def get_page(url):
#     """Get the content of a web page."""
#     response = requests.get(url)
#     try:
#         html_content =  response.content
#         soup = BeautifulSoup(html_content)
#         print(soup.prettify())
#     except Exception as e:
#         print("Error opening URL {}: {}".format(url, str(e)))
#         return None

driver.quit()