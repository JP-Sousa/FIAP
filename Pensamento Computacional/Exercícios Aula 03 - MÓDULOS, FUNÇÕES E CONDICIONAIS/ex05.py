"""▪ Faça um programa que leia 2 valores inteiros (A e B).
▪ A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando
se os valores lidos são múltiplos entre si.
Dica:
▪ Como que eu sei que 2 números são ou não são múltiplos um do outro?
▪ Conjunto dos Múltiplos de 2 = {2, 4, 6, 8, 10, ...}
▪ Então se observa que os múltiplos de um número são divisíveis por esse número, então o resto dessa
divisão será 0."""

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a % b == 0 or b % a == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")