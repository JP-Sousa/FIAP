# Contagem de 0 a 100 pulando de 10 em 10

n = int(input("Digite um numero inteiro positivo: "))

while i <= 100:
    print(i)
    i += 10

print()

for i in range(0, n+1, 10):
    print(i)