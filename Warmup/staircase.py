n = int(input().strip())
for i in range(1, n + 1):
    hash_tag = '#' * i
    space = ' ' * (n - i)
    print(space + hash_tag)
