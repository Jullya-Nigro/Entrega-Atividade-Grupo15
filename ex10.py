import requests
'''
10. Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
destino do passageiro ele retorne qual região de São Paulo aquele CEP é. Utilize a
documentação: https://viacep.com.br/
Exemplo: ao inserir o CEP 02122-050 o resultado deve ser a mensagem: Bairro: Vila Maria
Alta, Zona Norte de São Paulo.
As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro (indique também quando o
destino da corrida é pra fora da grande são paulo, em cidades vizinhas). Esse programa
será muito útil em relação à segurança dos motoristas, e com ele eles irão poder escolher
pra qual destino querem ou não aceitar corridas.
'''

cep = input("Digite o CEP do destino: ").replace("-", "").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    if "erro" in dados:
        print("CEP inválido.")
    else:
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "")
        uf = dados.get("uf", "")

        if cidade != "São Paulo":
            print(f"O destino é em {cidade}/{uf}, fora da Grande São Paulo.")
        else:
            print(f"Bairro: {bairro}, Zona desconhecida de São Paulo")
else:
    print("Erro ao consultar a API.")

