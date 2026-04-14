# Faça um programa que receba um número n
# Exiba a tabuada deste número do 0 ao 25.

n = int(input("Digite um numero inteiro positivo: "))

for i in range(1, 25+1, 1):
    print(f"{i} * {n} = {n*i}")