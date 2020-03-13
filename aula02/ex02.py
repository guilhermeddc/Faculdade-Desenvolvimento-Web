# 2. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salarioPorHora = float(input('Olá jovem! Diga quanto você ganha por hr?'))
hrsPorMes = float(input('Agora diga o número de hrs que você trabalha no mês:'))
salarioBruto = salarioPorHora * hrsPorMes

ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (ir + inss + sindicato) 

print(f'Seu sálario bruto é R${salarioBruto}')
print(f'Você pagou {inss} para o INSS')
print(f'Você pagou {ir} para o IR')
print(f'Você pagou {sindicato} para o sindicato')
print(f'Seu sálario liquido é R${salarioLiquido}')