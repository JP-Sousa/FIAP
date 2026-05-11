""" Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.

Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

Crie um programa em Python que:

 Percorra toda a matriz de temperaturas.

 Calcule a média de temperatura de cada sala.

 Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33.

 Mostre, para cada sala:

 número da sala;

 média das temperaturas;

 quantidade de registros críticos.



 Ao final, informe qual sala teve a maior quantidade de registros críticos.

 Considere que a primeira linha da matriz representa a Sala 1, a segunda linha representa a Sala 2, e assim por diante.

Saída esperada:
Sala 1
Média: 31.5
Registros críticos: 2

Sala 2
Média: 27.25
Registros críticos: 0

Sala 3
Média: 34.25
Registros críticos: 4

Sala 4
Média: 25.5
Registros críticos: 0


Sala com maior risco: Sala 3


Depois de desenvolvido, subir o arquivo python no github e enviar o link do seu repositório com o arquivo em python nomeado como: cp3.py """

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

media_sala = [0, 0, 0, 0]

qnt_temp_critica = [0, 0, 0, 0]

for i in range(len(temperaturas)):

    soma = 0

    for j in range(len(temperaturas[i])):
        soma += temperaturas[i][j]

        if temperaturas[i][j] >= 33:
            qnt_temp_critica[i] += 1

    print(soma)

    media_sala[i] = soma / len(temperaturas[i])

maior = qnt_temp_critica[0]
sala = i

for i in qnt_temp_critica:
    if i > maior:
        maior = qnt_temp_critica[i]
        sala = i

for i in range(len(temperaturas)):
    print(f"Sala {i+1}: Média das temperaturas {media_sala[i]}, quantidade de registros críticos: {qnt_temp_critica[i]}")

print(f"A sala que teve a maior quantidade de registros críticos foi a sala {sala}, com qnt_temp_critica{sala} registros acima de 33º")