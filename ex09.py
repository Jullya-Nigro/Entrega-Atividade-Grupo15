import requests
'''
9. Neste exercício, você irá criar um programa que solicita ao usuário a sigla de uma moeda
e exibe a cotação do Real (BRL) em relação a essa moeda. O objetivo é fazer uma
requisição à API de cotações de moedas, tratar a resposta e apresentar o valor do Real
em face da moeda escolhida. Você deve usar essa API: https://api.exchangerate-api.
com/v4/latest/BRL onde BRL é a sigla da moeda alvo (Real).
• Solicite ao usuário que insira a sigla da moeda desejada (por exemplo, “USD” para Dólar
Americano, “EUR” para Euro, “GBP” para Libra Esterlina, etc.).
• Faça uma requisição à API de cotações de moedas para obter a taxa de câmbio do Real
em relação à moeda informada pelo usuário.
• Extraia o valor da cotação do Real em relação à moeda solicitada.
• Exiba uma mensagem clara e informativa, como “O Real vale X [nome da moeda]”, onde
X é o valor da cotação. Ex: O Real vale 5.42 dólares americanos, traduzindo a sigla da
moeda para o nome completo (USD para dólares americanos).
'''

moeda = input("Digite a sigla da moeda: ").upper()

url = f"https://api.exchangerate-api.com/v4/latest/BRL"

response = requests.get(url)


if response.status_code == 200:
    dados = response.json()
    taxa = dados["rates"]

    if moeda in taxa:
        valor = taxa[moeda]
        print(f"O Real vale {valor:.2f} {moeda}")
    else:
        print("Moeda não encontrada na lista de cotações.")
else:
    print("Erro ao acessar a API.")

