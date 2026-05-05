"""▪ Escreva um algoritmo que recebe uma lista de nomes
e imprime os nomes na ordem inversa a da leitura.
 ▪ A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado. """

name = [" "]
i = 0

while True:
    name[i] = input("Digite um nome: ")
    if name[i] != "":
        i += 1
        name.append(name)
    else:
        break

for i in range(len(name) - 1, -1, -1):
    print(name[i])