"""▪ Determine e mostre todos os números primos no intervalo de 2 a 2000.
Dicas:
▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
primo ou não.
▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
no intervalo solicitado.
▪ Você precisará colocar uma estrutura de repetição dentro da outra.
▪ Laços aninhados!!!! """

def isEven(num):
    if num % 2 == 0:
        return True
    return False

def isPrime(num):

    if num == 2:
        return True

    if isEven(num):
        return False

    div = 0

    for i in range(1, num+1, 1):
        if num % i == 0:
           div += 1

    if div == 2:
        return True

    return False


num_range = int(input("Digite um número: "))

print(f"\nOs números primos entre 0 e {num_range} são:\n")

for i in range(num_range+1):

    if isPrime(i):
        print(f"{i},", end=" ")