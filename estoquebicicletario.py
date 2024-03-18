# Impressão do título do programa
print("Controle de Estoque - Bicicletaria Renata Moraes Cardoso (RU: xxxxxxx)")

# Lista para armazenar as peças cadastradas
listaPecas = []

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    # Dicionário para armazenar os dados da peça
    dicionarioPeca = {}

    print("Você selecionou a Opção de Cadastrar Peça")
    print("Código da peça é: 00{}".format(codigo))

    # Solicita os dados da peça ao usuário
    nome = input("Por favor entre com o NOME da peça: ")
    fabricante = input("Por favor entre com o FABRICANTE da peça: ")
    valor = float(input("Por favor entre com o VALOR (R$) da peça: "))

    # Preenche o dicionário com os dados da peça
    dicionarioPeca["codigo"] = codigo
    dicionarioPeca["nome"] = nome
    dicionarioPeca["fabricante"] = fabricante
    dicionarioPeca["valor"] = f'{valor:.2f}'

    # Adiciona o dicionário à lista de peças
    listaPecas.append(dicionarioPeca.copy())

# Função para consultar peças
def consultarPeca():
    while True:
        try:
            print("Você selecionou a Opção de Consultar Peças")
            consultar = int(input("Entre com a opção desejada: \n"
                                  "1-Consultar Todas as Peças \n"
                                  "2-Consultar Peças por Código \n"
                                  "3-Consultar Peças por Fabricante \n"
                                  "4-Retornar\n>>"))

            if consultar == 1:
                print("-"*20)
                # Itera sobre a lista de peças e exibe os dados de cada peça
                for peca in listaPecas:
                    for key, value in peca.items():
                        print("{} : {}".format(key, value))
                    print("-"*20)

            elif consultar == 2:
                print("-"*20)
                entrada = int(input("Digite o código desejado: "))
                for peca in listaPecas:
                    if peca["codigo"] == entrada:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
                        print("-"*20)

            elif consultar == 3:
                print("-"*20)
                entrada = input("Digite o fabricante desejado: ")
                for peca in listaPecas:
                    if peca["fabricante"] == entrada:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
                        print("-"*20)

            elif consultar == 4:
                break

            else:
                print("Digite uma opção válida")
                continue

        except ValueError:
            print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")

# Função para remover uma peça
def removerPeca():
    print("Você selecionou a Opção de Remover Peça")
    entrada = int(input("Digite o código da peça a ser removida: "))
    for peca in listaPecas:
        if peca["codigo"] == entrada:
            listaPecas.remove(peca)
            print("Peça removida.")

# Impressão do cabeçalho de boas-vindas
print("Bem-vindo(a) ao Controle de Estoque da Bicicletaria de Renata Moraes Cardoso (RU: xxxx)")

# Variável para controlar o código da peça
codigo = 0

while True:
    try:
        # Solicita a opção desejada ao usuário
        opcao = int(input("Escolha a opção desejada: \n"
                          "1-Cadastrar Peças \n"
                          "2-Consultar Peças \n"
                          "3-Remover Peças \n"
                          "4-Sair\n>>"))

        if opcao == 1:
            # Incrementa o código da peça e chama a função de cadastrar peça
            codigo += 1
            cadastrarPeca(codigo)

        elif opcao == 2:
            consultarPeca()

        elif opcao == 3:
            removerPeca()

        elif opcao == 4:
            print("Programa finalizado")
            break

        else:
            print("Digite uma opção válida")
            continue

    except ValueError:
        print("Digite uma opção válida. Digite valores inteiros para acessar a opção desejada.")