"""▪ Faça um programa que exiba a mensagem “Olá, Mundo”.
▪ Essa mensagem deverá ser exibida repetidamente.
▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário
 se ele deseja exibir a mensagem
novamente.
▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”."""

user_answer = "s"

while user_answer == 'S' or user_answer == "s":
    print("Olá, Mundo")

    user_answer = input("Deseja continuar exibindo a mensagem? (S) ou (N): ")

print("Fim")