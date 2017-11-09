n, arr = int(input()), []

for i in range(n):
    if i < n//2:
        arr.append((input().split(), False))
    else:
        arr.append((input().split(), True))

arr.sort(key=lambda x: int(x[0][0]))
arr = [i[0][1] if i[1] else '-' for i in arr]

print(*arr)
