linha1 = input().split(" ")
linha2 = input().split(" ")
x1, y1 = map(float, linha1)
x2 , y2 = map(float, linha2)


distancia = (((x2 - x1)**2  + (y2 - y1)**2))**0.5
print('{:.4f}'.format(distancia))