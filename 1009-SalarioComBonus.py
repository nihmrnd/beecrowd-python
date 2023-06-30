nome = input()
salarioFixo = float(input())
vendas = float(input())
vendaPorcentagem = (vendas * 15)/100
salarioTotal = vendaPorcentagem + salarioFixo
print('TOTAL = R$ {:.2f}'.format(salarioTotal))

