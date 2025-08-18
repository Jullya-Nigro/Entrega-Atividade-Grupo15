'''
5. O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

class Item:
    def __init__(self, especificacao, codigo, preco):
        self.especificacao = especificacao
        self.codigo = codigo
        self.preco = preco
        
class Conta:
    def __init__(self):
        self.itens = []
        
    def adicionar_item(self, item, quantidade):
        for _ in range(quantidade):
            self.itens.append(item)
    
    def calcular_total(self):
        return sum(item.preco for item in self.itens)
    
conta = Conta()
itens_disponiveis = [
    Item("Cachorro Quente", 100, 1.20),
    Item("bauru Simples", 101, 1.30),
    Item("bauru com Ovo", 102, 1.50),
    Item("Hambúrguer", 103, 1.20),
    Item("Cheeseburguer", 104, 1.30),
    Item("Refrigerante", 105, 1.00)
]

while True:
    print("Digite o codigo do item e sua quantidade")
    
    codigo = input("Codigo do item (ou 'sair' para finalizar): ")
    if codigo.lower() == 'sair':
        break
    
    quantidade = int(input("Quantidade: "))
    
    item_selecionado = next((item for item in itens_disponiveis if str(item.codigo) == codigo), None)
    if item_selecionado:
        conta.adicionar_item(item_selecionado, quantidade)
    else:
        print("Item não encontrado.")
    
print(f"Total a pagar: R${conta.calcular_total():.2f}")