"""Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a
média alcançada pelo aluno e apresentar:
▪ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
▪ A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
▪ A mensagem "Reprovado", se a média for menor que cinco."""

n1 = int(input("Digite a 1º nota: "))
n2 = int(input("Digite a 2º nota: "))
n3 = int(input("Digite a 3º nota: "))
n4 = int(input("Digite a 4º nota: "))

media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Em recuperação")
else:
    print("Reprovado")



