_, arr = input(), [int(i) for i in input().split()]


def insertion_sort(l):
    counter = 0
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            counter += 1
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return counter


print(insertion_sort(arr))
