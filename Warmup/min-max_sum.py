import sys

arr = sorted(list(map(int, input().strip().split(' '))))

print(sum(arr[:-1]),sum(arr[1:]))