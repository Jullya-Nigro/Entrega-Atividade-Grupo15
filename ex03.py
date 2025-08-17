nota01= float(input("Digite a primeira nota: "))
nota02= float(input("Digite a segunda nota: "))

media= (nota01 + nota02) / 2

if(media > 6):
    if(media > 9):
        print("Conceito A - Aprovado")
    elif(media > 7.5):
        print("Conceito B - Aprovado")
    elif(media > 6):
        print("Conceito C - Aprovado")
else:
    if(media > 4):
        print("Conceito D - Reprovado")
    else:
        print("Conceito E - Reprovado")
        
