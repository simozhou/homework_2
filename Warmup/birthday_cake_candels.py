n = int(input().strip())
height = list(map(int, input().strip().split(' ')))
print(height.count(max(height)))
