_, arr = input(), sorted([int(i) for i in input().split()])


def is_even(n):
    return bool(n % 2)


if is_even(len(arr)):
    print(arr[len(arr)//2])
else:
    print(arr[(len(arr)+1)//2])
