#Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário

n = int(input("Digite um numero inteiro positivo: "))

for i in range(2, n+1, 2):
        print(f"{i}", end=" ")