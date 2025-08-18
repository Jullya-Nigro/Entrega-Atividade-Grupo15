'''
7. Faça um programa que leia um número indeterminado de valores numéricos, encerrando
a entrada de dados quando for informado um valor igual a −1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
• Mostre a quantidade de valores que foram lidos;
• Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
• Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
• Calcule e mostre a soma dos valores;
• Calcule e mostre a média dos valores;
• Calcule e mostre a quantidade de valores acima da média calculada;
'''

numeros = []

while True:
    try:
        numero = int(input("Digite um número (-1 para parar): "))
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue

    if numero != -1:
        numeros.append(numero)
    else:
        if not numeros:
            print("Nenhum número foi informado.")
            break

        print("Quantidade de valores que foram lidos:", len(numeros))

        print("Todos os valores na ordem em que foram informados:")
        for o in numeros:
            print(o, end=" ")
        print()

        print("Todos os valores na ordem inversa à que foram informados:")
        for i in reversed(numeros):
            print(i, end=" ")
        print()

        print("A soma dos valores:", sum(numeros))

        media = sum(numeros) / len(numeros)
        print("A média dos valores:", media)

        numeros_acima_media = sum(1 for n in numeros if n > media)
        print("A quantidade de valores acima da média calculada:", numeros_acima_media)

        break

