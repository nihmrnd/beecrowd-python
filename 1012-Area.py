pi = 3.14159
linha1 = input().split(" ")
a,b,c = linha1

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c) * float(c))
trapezio = ((float(a) + float(b)) * float(c))/2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))