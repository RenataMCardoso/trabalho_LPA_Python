#Boas vindas
print('Seja bem vindo a loja da Renata Moraes Cardoso (RU 4362789)')
#Solicito o preço do produto
preco = float(input("Digite o preço do protudo: R$"))
#Solicito a quantidade do produto
qnt = int(input('Digite a quantidade do procuto:'))
desconto = 0

#Se a quantidade do produto for menor ou igual ao 9 o desconto será de 0%
if qnt <= 9:
  desconto = 0.00
#E se for maior ou igual a 10 e menor ou igual a 99 o desconto será de 5%
elif (qnt>= 10) and (qnt <=99):
  desconto = 0.05
#E se for menor ou igual a 100 e menor ou igual a 999 o desconto será 10%
elif (qnt <= 100) and (qnt <= 999):
  desconto = 0.10
#Caso contrario a isso tudo o desconto será de 15%, ou seja, maior que 1000 peças
else:
  desconto = 0.15

#Na variavel total pegamos o preço vezes a quantidade, para saber o valor total
#sem desconto e logo em sequencia informamos ao cliente o valor sem desconto
total = preco * qnt
print('O valor do produto sem desconto é de: R$ {:.2f}' .format(total))
#Na variavel totalcomdesconto pegamos o valor com a porcentagem que é o valor total
#menos o valor total vezes o desconto e informamos o valor com desconto
totalcomdesconto = total - total * desconto
print('O valor do produto com desconto é de: R$ {:.2f}'.format(totalcomdesconto))