import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_temp = map(int,input().strip().split(' '))
    a.append(a_temp)
h, w = len(a), len(a[0])
d = 0
sd = 0
for i in range(h):
    for j in range(w):
        if i == j and (i + j) == (w-1):
            d += a[i][j]
            sd += a[i][j]
        elif i == j:
            d += a[i][j]
        elif (i+j) == (w-1):
            sd += a[i][j]

print(abs(d - sd))