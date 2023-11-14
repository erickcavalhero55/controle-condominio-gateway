import requests

url = 'http://54.167.214.72/veiculo/1'

user_veiculo = {
    "placa": "121213",
    "marca": "Silva",
    "nome_veiculo": 4564488961,
    "cor": 56547899546,
    "id_usuarios": 11125546985

}


response = requests.post(url=url, json=user_veiculo)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
