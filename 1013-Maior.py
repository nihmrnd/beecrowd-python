linha1 = input().split(" ")
a,b,c = linha1

maiorAB = (int(a) + int(b) + abs(int(a) - int(b)))/2
if int(c) > maiorAB:
  maiorAB = int(c)

print(int(maiorAB),'eh o maior')