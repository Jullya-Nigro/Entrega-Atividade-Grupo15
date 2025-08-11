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