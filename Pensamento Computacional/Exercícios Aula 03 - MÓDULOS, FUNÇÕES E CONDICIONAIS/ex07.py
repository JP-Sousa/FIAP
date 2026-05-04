"""Faça um programa que receba o ano de nascimento da pessoa e retorne:
▪ Se o voto é obrigatório este ano;
▪ Se o voto é opcional este ano;
▪ Se o voto é proibido este ano."""

year = int(input("Digite o ano de nascimento: "))
age = 2026 - year

if age < 16:
    print("Menor de idade, não pode votar")
elif (age >= 16 and age < 18) or (age >= 70):
    print("Voto Opcional")
else:
    print("Voto Obrigatório")