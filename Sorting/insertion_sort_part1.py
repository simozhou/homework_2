def insertion_sort(arr: list) -> None:
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            val = arr[i]
            arr[i] = arr[i - 1]
            print(*arr)
            arr[i - 1] = val
    else:
        print(*arr)


insertion_sort([int(i) for i in input().split()])
