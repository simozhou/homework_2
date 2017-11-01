import sys
from collections import defaultdict

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)

# dictionary str: length of the string, number itself
# MODUS OPERANDI: sort by lenght first, then each size sorted by itself
d = defaultdict(list)
for i in unsorted:
    d[len(i)].append(i)

for k, v in d.items():
    d[k] = sorted(v)

for i in sorted(d.items(), key=lambda x: x[0]):
    print(*i[1], sep='\n')