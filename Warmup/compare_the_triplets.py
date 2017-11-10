a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
l1 = [a0, a1, a2]
l2 = [b0, b1, b2]
alice = 0
bob = 0
lst = zip(l1, l2)
for i in lst:
    if i[0] == i[1]:
        continue
    elif i[0] > i[1]:
        alice += 1
    else:
        bob += 1
print(alice, bob)
