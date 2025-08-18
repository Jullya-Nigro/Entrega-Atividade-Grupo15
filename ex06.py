'''
6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
• Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

ano_inicio = 1995

try:
    salario_inicial = float(input("Digite o salário inicial do funcionário: "))
except ValueError:
    print("Erro: digite um valor numérico válido para o salário.")
    salario_inicial = 1000.0  
    print(f"Usando salário inicial padrão: R$ {salario_inicial:.2f}")

salario = salario_inicial
percentual_aumento = 1.5  

for ano in range(1996, 2025):  
    aumento = salario * (percentual_aumento / 100)
    salario += aumento
    percentual_aumento *= 2

print(f"O salário atual do funcionário é: R$ {salario:.2f}")
