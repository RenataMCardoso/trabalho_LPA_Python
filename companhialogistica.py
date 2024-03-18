# Exibe uma mensagem de boas-vindas
print("Bem-vindo(a) à Companhia de Logística Renata Moraes Cardoso (RU:xxxxxx)")
# Função para calcular as dimensões do objeto e retornar a tarifa correspondente
def dimensoesObjeto():
    while True:
        try:
          # Captura as dimensões do objeto
            comprimento = float(input("Digite o comprimento do objeto em cm: "))
            largura = float(input("Digite a largura do objeto em cm: "))
            altura = float(input("Digite a altura do objeto em cm: "))
               # Calcula o volume do objeto
            volume = altura * comprimento * largura
            print(f"O volume do objeto em cm³ é: {volume}")

            # Determina a tarifa com base no volume
            if volume < 1000:
                return 10, volume
            elif 1000 <= volume < 10000:
                return 20, volume
            elif 10000 <= volume < 30000:
                return 30, volume
            elif 30000 <= volume < 100000:
                return 50, volume
            else:
                print("Não aceitamos objetos com dimensões tão grandes")
                print("Entre com as dimensões desejadas novamente")

                # Função para calcular o peso do objeto e retornar a tarifa correspondente
        except ValueError:
            print("Você digitou alguma dimensão do objeto com valor não numérico")
            print("Por favor, entre com as dimensões desejadas novamente")

def pesoObjeto():
    while True:
        try:
          # Captura o peso do objeto
            peso = float(input("Digite o peso do objeto em kg: "))
            print(f"O peso do objeto em kg é: {peso}")

             # Determina a tarifa com base no peso
            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print("Não aceitamos objetos tão pesados")
                print("Por favor, entre com as dimensões desejadas novamente")
        except ValueError:
            print("Você digitou um peso do objeto com valor não numérico")
            print("Por favor, entre com as dimensões desejadas novamente")


# Função para definir a rota do objeto e retornar a taxa correspondente
def rotaObjeto():
    print("Selecione a rota:")
    print("BR - De Brasília para Rio de Janeiro")
    print("BS - De Brasília para São Paulo")
    print("RB - De Rio de Janeiro para Brasília")
    print("RS - De Rio de Janeiro para São Paulo")
    print("SR - De São Paulo para Rio de Janeiro")
    print("SB - De São Paulo para Brasília")

    while True:
        rotas = {
            "RS": 1,
            "SR": 1,
            "BS": 1.2,
            "SB": 1.2,
            "BR": 1.5,
            "RB": 1.5
        }
        rota = input("Digite a rota desejada: ")

        if rota in rotas:
            return rotas[rota]
        else:
            print("Você digitou uma rota que não existe.")
            print("Por favor, entre com a rota desejada novamente")

dimensoes, volume = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
valorTotal = dimensoes * peso * rota
print("Valor total a ser pago: R$", valorTotal)