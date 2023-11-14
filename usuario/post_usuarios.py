import requests

url = 'http://54.167.214.72/usuario/3'

user_usuario ={
    "nome": "renasvdgsgfgsdfgsfdgvsdvsdvsdvsdvsdvsdvxxxxn",
    "sobrenome": "Silva",
    "rg": 4564488961,
    "cpf": 56547899546,
    "telefone": 11125546985,
    "celular": 11954879859,
    "email": "Joaosilva@gmail.com",
    "genero": "masculino"
}
response = requests.post(url=url, json=user_usuario)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
