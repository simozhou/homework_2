_, arr = input(), [int(i) for i in input().split()]


def quick_sort(array):
    # base case
    if len(array) <= 1:
        return array
    # division and recursive step
    else:
        pivot = array.pop(0)
        left, right = [], []
        for element in array:
            if element < pivot:
                left.append(element)
            else:
                right.append(element)
        return quick_sort(left) + [pivot] + quick_sort(right)


print(*quick_sort(arr), sep=' ')
