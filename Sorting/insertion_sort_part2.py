_, a = input(), [int(i) for i in input().split()]


def insertion_sort2(arr: list) -> None:
    for i in range(1, len(arr)):
        hold = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > hold:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = hold
        print(*arr)


insertion_sort2(a)
