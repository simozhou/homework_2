import sys


s = input().strip()
def camelCounter(s):
    c = 1
    for i in s:
        if i.isupper():
            c+=1
    return c

print(camelCounter(s))