from bs4 import BeautifulSoup
import requests
from selenium import webdriver





login_url = 'https://winwins.app/#/login'
target_url = 'https://winwins.app/#/win'

payload = {
    'mobilenumber':'9370664563',
    'password':'@Sniper9370',
}

with  requests.Session() as s:
    driver = webdriver.Chrome()
    driver.get(login_url)
    driver.implicitly_wait(5)
    s.post(login_url, data=payload)
    r = s.get(target_url)
    soup = BeautifulSoup(r.content, 'html.parser') 
    print(soup.prettify())
    driver.quit()