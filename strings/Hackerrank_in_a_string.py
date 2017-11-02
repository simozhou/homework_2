proof = list('hackerrank')
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    cnt = 0
    for i in proof:
        try:
            placeHolder = s.index(i)
        except ValueError:
            print("NO")
            break
        s = s[placeHolder + 1:]
        cnt += 1
    if cnt == len(proof):
        print("YES")
