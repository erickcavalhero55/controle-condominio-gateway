import requests

url = 'http://54.167.214.72/encomenda/1'

user_encomendas ={
            "titulo": "Mercado livre",
            "tipo": "caixa",
            "nota_fiscal": "123245658",
            "id_usuarios": "1"
 }
response = requests.put(url=url, json=user_encomendas)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)







