age = int(input("Digite sua idade: "))

if age < 16:
    print("Menor de idade, não pode votar")
elif (age >= 16 and age < 18) or (age >= 70):
    print("Voto Opcional")
else:
    print("Voto Obrigatório")