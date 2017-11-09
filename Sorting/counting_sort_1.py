_, arr = input(), [int(i) for i in input().split()]


def count_me_in(a: list) -> None:
    d, hold = {i: 0 for i in range(100)}, []
    for elem in a:
        if elem in d:
            d[elem] += 1
    print(*d.values())


count_me_in(arr)
