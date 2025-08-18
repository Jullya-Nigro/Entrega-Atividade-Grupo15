'''
3. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:

Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero e

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for
D ou E.
'''


try:
    nota01 = float(input("Digite a primeira nota: "))
    nota02 = float(input("Digite a segunda nota: "))

    if nota01 < 0 or nota01 > 10 or nota02 < 0 or nota02 > 10:
        raise ValueError("As notas devem estar entre 0 e 10.")

    media = (nota01 + nota02) / 2
    if media > 6:
        if media > 9:
            print("Conceito A - Aprovado")
        elif media > 7.5:
            print("Conceito B - Aprovado")
        else: 
            print("Conceito C - Aprovado")
    else:
        if media > 4:
            print("Conceito D - Reprovado")
        else:
            print("Conceito E - Reprovado")

except ValueError as ve:
    print(f"Erro: {ve}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
