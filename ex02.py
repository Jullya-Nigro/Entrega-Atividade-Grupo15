'''
2. Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
na máquina.
• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

notas = [100, 50, 20, 10, 5, 1]

def entregar_notas(quantidade, notas):
    return quantidade // notas, quantidade % notas

def sacar(quantidade):
    notas_sacadas = {}
    
    if quantidade < 10:
        print("Saque não realizado, minimo permitido é 10!")
        
        return notas_sacadas
        
    elif quantidade > 600:
        print("Saque não realizado, máximo permitido é 600!")
        
        return notas_sacadas

    restante = quantidade
    for nota in notas:
        quantidade_de_notas, restante = entregar_notas(restante, nota)
    
        notas_sacadas[nota] = quantidade_de_notas
        
        if restante == 0:
            break

    return notas_sacadas

quantidade = input("Digite o valor do saque: ")

try:
    quantidade = int(quantidade)
    notas_sacadas = sacar(quantidade)

    if len(notas_sacadas) > 0:
        for nota, quantidade in notas_sacadas.items():
            if quantidade > 0:
                print(f"{quantidade} nota(s) de R${nota}")
    
except ValueError:
    print("Valor inválido, por favor digite um número inteiro.")