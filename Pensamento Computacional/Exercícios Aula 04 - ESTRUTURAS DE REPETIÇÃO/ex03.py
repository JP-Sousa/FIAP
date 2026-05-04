# Faça um programa que receba um número n
# Exiba a tabuada deste número do 0 ao 25.

n = int(input("Digite um numero: "))

for i in range(26):
    print(f"{n} * {i} = {n*i}")