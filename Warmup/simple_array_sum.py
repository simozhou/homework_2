def sum_lst(lst):
    return sum(lst)


n = int(input().strip())
arr = map(int, input().strip().split(' '))
print(sum_lst(arr))
