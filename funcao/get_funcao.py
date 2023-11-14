import requests

url = 'http://54.167.214.72/funcoe/1'

user_cobranca = {



}

response = requests.get(url=url, json=user_cobranca)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)