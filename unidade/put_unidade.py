import requests

url = 'http://54.167.214.72/unidade/1'

user_unidade= {
    "numero": 45,
    "bloco": "c",
    "andar": 3,
    "id_usuarios": "1"
}


response = requests.post(url=url, json=user_unidade)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
