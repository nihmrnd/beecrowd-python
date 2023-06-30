linha1 = input().split(" ")
linha2 = input().split(" ")
cod1,qnt1,val1 = linha1
cod2,qnt2,val2 = linha2
total = (int(qnt1) * float(val1)) + (int(qnt2) * float(val2))
print('VALOR A PAGAR: R$ {:.2f}'.format(total))