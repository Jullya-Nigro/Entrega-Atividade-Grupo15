'''
1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
• até 20 litros: desconto de 3% por litro
• acima de 20 litros: desconto de 5% por litro
Gasolina:
• até 20 litros: desconto de 4% por litro
• acima de 20 litros: desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

def calculo_combustivel(combustivel, litros):
    if combustivel == "g":
        valor = litros * 2.50
        if litros <= 20:
            valor_total = valor - (valor * 0.03) 
        else:
            valor_total = valor - (valor * 0.05) 

    elif combustivel == "a":
        valor = litros * 1.90
        if litros <= 20:
            valor_total = valor - (valor * 0.04) 
        else:
            valor_total = valor - (valor * 0.06) 
    else:
        raise ValueError("Combustível inválido! Use 'g' para gasolina ou 'a' para álcool.")
    
    return valor_total

try:
    combustivel = input("Qual é o combustível | a- álcool, g- gasolina: ").lower().strip()
    litros = float(input("Quantos litros?: "))

    if litros <= 0:
        raise ValueError("Quantidade de litros deve ser maior que zero.")

    valor_combustivel = calculo_combustivel(combustivel, litros)
    print(f"O valor do combustível é: R$ {valor_combustivel:.2f}")

except ValueError as ve:
    print(f"Erro: {ve}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
