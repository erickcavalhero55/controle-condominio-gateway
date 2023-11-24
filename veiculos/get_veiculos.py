import requests

url = 'http://54.167.214.72/veiculo/'

response = requests.get(url=url, json=user_cobranca)

if 200 <= response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)


