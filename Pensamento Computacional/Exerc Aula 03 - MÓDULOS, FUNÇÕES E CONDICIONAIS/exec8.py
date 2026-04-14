"""Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:
▪ Salários até R$ 280,00 (incluindo): aumento de 20%.
▪ Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
▪ Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
▪ Salários de R$ 1500,00 em diante: aumento de 5%.
▪ Após o aumento ser realizado, informe na tela:
▪ O salário antes do reajuste.
▪ O percentual de aumento aplicado.
▪ O valor do aumento.
▪ O novo salário, após o aumento"""

wage = float(input("Digite o salário: "))
oldWage = wage

if wage <= 280:
    percentual = 1.2
    wage *= percentual
elif wage > 280 and wage <= 700:
    percentual = 1.15
    wage *= percentual
elif wage > 700 and wage <= 1500:
    percentual = 1.10
    wage *= percentual
else:
    percentual = 1.05
    wage *= percentual

print(f"\nSalário antigo: R$ {oldWage:.2f}\nPercetual de ajuste: {percentual}\nValor do Aumento: R${wage-oldWage:.2f}\nNovo Salário: R${wage:.2f}")