import requests

url = 'http://54.167.214.72/funcoe/1'

user_funcoes = {

        "nome": "jvsdvdsvose",
        "sobrenome": "jose",
        "cpf": 5648654165,
        "end_cliente": 150,
        "cnh": 90

}
response = requests.put(url=url, json=user_funcoes)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)

