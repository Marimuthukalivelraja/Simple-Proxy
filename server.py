import requests
from requests.exceptions import ProxyError, ConnectTimeout, HTTPError


#proxy server address
proxies = {
    'http': 'http://144.217.101.245:3128',
    'https': 'http://144.217.101.245:8080'
}

try:
    response = requests.get("https://ipinfo.io/json/", proxies=proxies, timeout=10)
    response.raise_for_status() 
    print(response.text)
except ProxyError:
    print("Error: Unable to connect to the proxy.")
except ConnectTimeout:
    print("Error: Connection timed out.")
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
