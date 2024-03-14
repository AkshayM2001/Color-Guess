from pprint import pprint
import requests
from config import user,password
from bs4 import BeautifulSoup

def main():
    url = 'https://winwins.app/#/login'

    with requests.session() as session:
        # response = session.post(url, auth=(user, password))
        response = session.post(url)

        # pprint(response.text)

        password = password + ':'
        user = user + ':'

        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'id':'authForm'})

        # csrf_input = form.find('input', {'name': '_csrf'})
        # method_input = form.find('input', {'name': '_method'})

        data = {  
            'username': user, 
            'password': password,  
            # '_csrf': csrf_input['value'], 
            # '_method': method_input['value'] if method_input else None
        }
        
        print("Logging in...")
        login_response = session.post(url, data=data)

        # Check to see if we were successful


        with open('index.html', 'w') as f:
            f.write(response.text)