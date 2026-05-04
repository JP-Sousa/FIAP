"""▪ Faça um programa que recebe:
▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
▪ o peso da carga do caminhão em toneladas
▪ o código da carga, supondo que é um número inteiro de 10 e 40
▪ Seu programa deve calcular:
▪ o peso da carga do caminhão convertido em quilos
▪ o preço da carga do caminhão
▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
▪ o valor total transportado pelo caminhão (carga + impostos)

1 35%
2 25%
3 15%
4 5%
5 isento

10a20 100
21a30 250
31a40 340
"""

state_code = int(input("Digite o Estado de origem da carga (1 a 5): "))
weight = float(input("Digite o peso da carga (em toneladas): "))
weight_code = int(input("Digite o código da carga (10 a 40): "))

weight *= 1000

if weight_code >= 10 and weight_code <= 20:
    price = 100
elif weight_code >= 21 and weight_code <= 30:
    price = 250
elif weight_code >= 31 and weight_code <= 40:
    price = 340

total_price = weight * price

match state_code:

    case 1:
        tax = 0.35
    case 2:
        tax = 0.25
    case 3:
        tax = 0.15
    case 4:
        tax = 0.05
    case 5:
        tax = 0

total_tax = total_price * tax

total_value = total_price - total_tax

print(f"\nCarga: {weight/1000}t\nEstado: {state_code}\nCódigo de peso: {weight_code}"
      f"\nImposto: R${total_tax:,}\nValor da carga: R${total_price:,}\nValor total: R${total_value:,}")