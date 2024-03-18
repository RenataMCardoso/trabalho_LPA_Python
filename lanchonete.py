# Função para imprimir o menu de dar boas vindas
def menu():
    print("Bem-Vindo(a) à Lanchonete da Renata Moraes Cardoso (RU:xxxxxx)")
    print(15 * "" + "Cardápio" + 15 * "")
    print("| Código | Descrição          | Valor  |")
    print("| 100    | Cachorro Quente    | 9,00   |")
    print("| 101    | Cachorro Quente Duplo | 11,00 |")
    print("| 102    | X-Egg              | 12,00  |")
    print("| 103    | X-Salada           | 12,00  |")
    print("| 104    | X-Bacon            | 14,00  |")
    print("| 105    | X-Tudo             | 17,00  |")
    print("| 200    | Refrigerante Lata  | 5,00   |")
    print("| 201    | Chá Gelado         | 4,00   |")

# Variável para armazenar o valor total do pedido
valorPedido = 0

# Função que atualiza o pedido
def atualizaPedido(valorPedido, tipoProduto, valorProduto4302056):
    valorAtualizado = valorPedido + valorProduto4302056
    print(f"Você pediu um {tipoProduto} no valor de {valorProduto4302056}")
    return valorAtualizado

# Chamada inicial do menu
menu()

# Loop para receber os códigos dos produtos e atualizar o pedido
while True:
    codigo = int(input("Entre com o código desejado: "))

    # Verifica qual produto corresponde ao código fornecido
    if codigo == 100:
        tipoProduto = "Cachorro Quente"
        valorProduto4302056 = 9
    elif codigo == 101:
        tipoProduto = "Cachorro Quente Duplo"
        valorProduto4302056 = 11
    elif codigo == 102:
        tipoProduto = "X-Egg"
        valorProduto4302056 = 12
    elif codigo == 103:
        tipoProduto = "X-Salada"
        valorProduto4302056 = 12
    elif codigo == 104:
        tipoProduto = "X-Bacon"
        valorProduto4302056 = 14
    elif codigo == 105:
        tipoProduto = "X-Tudo"
        valorProduto4302056 = 17
    elif codigo == 200:
        tipoProduto = "Refrigerante Lata"
        valorProduto4302056 = 5
    elif codigo == 201:
        tipoProduto = "Chá Gelado"
        valorProduto4302056 = 4
    else:
        print("Opção inválida")
        continue

    # Atualiza o valor total do pedido
    valorPedido = atualizaPedido(valorPedido, tipoProduto, valorProduto4302056)

    # Pergunta se o cliente deseja pedir mais algum produto
    print("Deseja pedir mais alguma coisa?")
    print("1- Sim")
    print("0- Não")
    resposta = int(input(""))

    if resposta == 1:
        continue
    elif resposta == 0:
        print(f"O valor total é: {valorPedido}")
        break