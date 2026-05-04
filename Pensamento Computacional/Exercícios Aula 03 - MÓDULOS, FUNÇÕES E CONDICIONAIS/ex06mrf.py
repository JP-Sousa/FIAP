"""Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
matemáticas (+, -, *, /)
▪ O programa deve calcular o valor final de acordo com a operação selecionada.
▪ Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30."""

def som(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
operator = input("Digite o símbolo da operação desejada(+, -, *, /): ")
result = None

match operator:

    case "+":
        result = som(num1, num2)
    case "-":
        result = sub(num1, num2)
    case "*":
        result = mul(num1, num2)
    case "/":
        result = div(num1, num2)

if result is None:
    print("Operação inexistente")
else:
    print(f"O resultado de {num1} {operator} {num2} é {result:.2f}")