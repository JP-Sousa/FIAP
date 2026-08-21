import random

random.seed(0)

numeros = [random.randint(1, 200) for _ in range(200)]

random.shuffle(numeros)

def bubble_sort(lista):

    n = len(lista)

    trocas = 0

    for i in range(n):
        for j in range(n-1-i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, trocas

def selection_sort(lista):

    n = len(lista)

    trocas = 0

    for i in range(n):

        menor = i

        for j in range(i+1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
        trocas += 1

    return lista, trocas

def insertion_sort(lista):

    trocas = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:

            lista[j + 1] = lista[j]
            trocas += 1
            j -= 1

        lista[j+1] = atual

    return lista, trocas

def imprimir_lista(lista):
    for i in range(0, len(lista), 20):
        print(*lista[i:i + 20])

print("Lista desordenada: ")
imprimir_lista(numeros)

lista, trocas = bubble_sort(numeros.copy())

print("\nBubble Sort:\n")
imprimir_lista(lista)
print("\nTrocas: ", trocas)

lista, trocas = selection_sort(numeros.copy())

print("\nSelection Sort:\n")
imprimir_lista(lista)
print("\nTrocas: ", trocas)

lista, trocas = insertion_sort(numeros.copy())

print("\nInsertion Sort:\n")
imprimir_lista(lista)
print("\nTrocas: ", trocas)