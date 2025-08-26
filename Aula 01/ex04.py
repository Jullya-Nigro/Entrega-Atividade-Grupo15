'''
4. Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
questões. O programa deve seguir os seguintes passos:
• Perguntar ao aluno a resposta de cada uma das 10 questões.
• Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
• Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta.
• Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova.
Após todos os alunos terem respondido, o programa deve informar:
• O maior e o menor número de acertos entre os alunos.
• O total de alunos que utilizaram o sistema.
• A média das notas da turma.
'''

def pega_respostas():
    gabarito_aluno = []
    for i in range(1, 10+1):
        while True:
            nota = input(f"{i}ª QUESTÃO (a, b ou c): ").lower().strip()
            if nota in ["a", "b", "c"]:
                gabarito_aluno.append(nota)
                break
            else:
                print("Resposta inválida! Digite apenas 'a', 'b' ou 'c'.")
    return gabarito_prova(gabarito_aluno)

def gabarito_prova(gabarito_aluno):
    acertos = 0
    gabarito = ["a", "b", "c", "a", "b", "c", "c", "b", "a", "a"]
    for resp_aluno, resp_correta in zip(gabarito_aluno, gabarito):
        if resp_aluno == resp_correta:
            acertos += 1
    return acertos

nota_alunos = []
while True:
    pergunta_prova = input("Deseja fazer a prova? s- sim | n- não: ").lower().strip()
    if pergunta_prova == "s":
        acertos = pega_respostas()
        nota_alunos.append(acertos)
    elif pergunta_prova == "n":
        if nota_alunos:
            media = sum(nota_alunos) / len(nota_alunos)
            print(f"O maior número de acertos entre os alunos é: {max(nota_alunos)}")
            print(f"O menor número de acertos entre os alunos é: {min(nota_alunos)}")
            print(f"A média das notas da turma é: {media:.2f}")
        else:
            print("Nenhum aluno fez a prova.")
        break
    else:
        print("--RESPOSTA INVÁLIDA! Digite 's' ou 'n'.--")
