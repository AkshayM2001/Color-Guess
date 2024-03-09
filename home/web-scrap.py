from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

url = 'https://winwins.app/#/login'

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

response = requests.get(url)
html_content =  response.content
soup = BeautifulSoup(html_content)
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