import requests

'''
8. Faça chamada à API restcountries, que retorna informações sobre países, extraia essas
informações para as manipular conforme orientações abaixo. Por exemplo, ao acessar
https://restcountries.com/v3.1/name/brazil, onde brazil é o país escolhido, é retor-
nado em JSON vários dados sobre o Brasil, em posse disso você deve exibir no programa
que criará:
• Nome do país (Brasil), linguagem(s) (“Portuguese”...), região (“Americas”), subregião
(“South America”) com a capital (“Brasilia”)
• Sigla da moeda (BRL), nome (“Brazilian real”) e símbolo da moeda (“R$”)
• Países que fazem fronteira com o Brasil: “ARG”, “BOL”, “COL”, “GUF”, “GUY” ...
Permita que o usuário insira o nome do país (ex: italy, zambia, japan, canada, germany) e
são retornados esses dados.
''' 

pais = input("Digite o nome do país que deseja obter informações: ").strip()

url = f"https://restcountries.com/v3.1/name/{pais}"

try:
    response = requests.get(url)
    response.raise_for_status()  

    dados = response.json()[0]

    nome = dados["name"]["common"]
    linguagens = ", ".join(dados.get("languages", {}).values()) or "Não informado"
    regiao = dados.get("region", "Não informado")
    subregiao = dados.get("subregion", "Não informado")
    capital = ", ".join(dados.get("capital", [])) or "Não informado"

    
    moedas = dados.get("currencies", {})
    if moedas:
        sigla_moeda = list(moedas.keys())[0]
        moeda = moedas[sigla_moeda]
        nome_moeda = moeda.get("name", "Não informado")
        simbolo_moeda = moeda.get("symbol", "Não informado")
    else:
        sigla_moeda = nome_moeda = simbolo_moeda = "Não informado"

   
    fronteiras = ", ".join(dados.get("borders", [])) or "Não possui"

    print(f"""
Nome do país: {nome}
Linguagem(s): {linguagens}
Região: {regiao}
Subregião: {subregiao}
Capital: {capital}
Sigla da moeda: {sigla_moeda}
Nome da moeda: {nome_moeda}
Símbolo da moeda: {simbolo_moeda}
Fronteiras: {fronteiras}
""")

except requests.exceptions.HTTPError:
    print(f"Erro: Não foi possível encontrar informações para o país '{pais}'.")
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro ao acessar a API: {e}")
except (KeyError, IndexError):
    print("Erro ao processar os dados recebidos da API.")
