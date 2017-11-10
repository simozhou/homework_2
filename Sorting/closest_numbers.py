n, arr = input(), sorted([int(i) for i in input().split()])

lowest = abs(arr[0] - arr[1])
result = [arr[0], arr[1]]

for i in range(1, len(arr) - 1):
    difference = abs(arr[i + 1] - arr[i])
    if difference < lowest:
        result = [arr[i], arr[i + 1]]
        lowest = difference
    elif difference == lowest:
        result.append(arr[i])
        result.append(arr[i + 1])

print(*result)
