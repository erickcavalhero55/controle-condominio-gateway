import requests

url = 'http://54.167.214.72/usuario/1'

user_usuario = {

        "nome": "josevdvds",
        "sobrenome": "jose",
        "cpf": 56486541655,
        "end_cliente": 150,
        "cnh": 90

}
response = requests.put(url=url, json=user_usuario)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
