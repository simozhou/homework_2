def super_reduced_string(string):
    """implemented using a stack"""
    res = []  # stack
    for c in string:
        if res and res[len(res)-1] == c:
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or 'Empty String'


s = input().strip()
result = super_reduced_string(s)
print(result)
