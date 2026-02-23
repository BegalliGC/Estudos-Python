from cmath import inf
n = int(input())

fita = list(map(int,input().split()))

distancias = [float('inf')] *n


zero_mais_prox = float('inf')
for i in range(n):
    if fita[i] == 0:
        zero_mais_prox = 0
        distancias[i] = 0
    else:
        if zero_mais_prox != float('inf'):
            zero_mais_prox += 1
            distancias[i] = min(distancias[i], zero_mais_prox)


zero_mais_prox = float('inf')
for i in range(n-1,-1,-1):
    if fita[i] == 0:
        zero_mais_prox = 0
        distancias[i] = 0
    else:
        if zero_mais_prox != float('inf'):
            zero_mais_prox += 1
            distancias[i] = min(distancias[i], zero_mais_prox)

for i in range(n):
    if fita[i] == -1:
        if distancias[i] >= 9:
            fita[i] = 9
        else:
            fita[i] = distancias[i]

print(' '.join(map(str,fita)))