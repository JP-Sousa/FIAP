"""Faça um programa que tenha 2 vetores.
Um vetor para os meses e outros para a quantidade de dias para cada mês.
 ▪ Seu programa deve exibir mensagens da seguinte forma: ▪ O Mês de Jan tem 31 dias atodo.
 ▪ O mês de Fev tem 28 dias ao O mês de Mar tem 31 dias ao ▪ O mês de Mar tem 31 dias ao to do.
  ▪ ... ▪ O mês de Dez tem 31 dias ao to do."""

months = ["janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"]

total_days = [
    31,  # janeiro
    28,  # fevereiro
    31,  # março
    30,  # abril
    31,  # maio
    30,  # junho
    31,  # julho
    31,  # agosto
    30,  # setembro
    31,  # outubro
    30,  # novembro
    31   # dezembro
]

for _ in range(len(months)):
    print(f"O Mês de {months[_]} tem {total_days[_]} dias ao todo")