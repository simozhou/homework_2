n = int(input().strip())
arr = map(int, input().strip().split(' '))
pos, neg, zeros = map(len, (filter(lambda x: x > 0, arr),
                            filter(lambda x: x < 0, arr), filter(lambda x: x == 0, arr)))

print("{0:.6f}".format(pos / float(n)))
print("{0:.6f}".format(neg / float(n)))
print("{0:.6f}".format(zeros / float(n)))
