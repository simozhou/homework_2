#!/bin/python3
import sys


def counting_sort(lst):
    min_lst = min(lst)
    k = (max(lst) - min_lst) + 1
    C = [0] * k
    for i in lst:
        C[i - min_lst] += 1

    hold = []
    for i, v in enumerate(C):
        hold += [i] * v
    return hold


def median(arr):
    arr = counting_sort(arr)
    size = len(arr)
    if size % 2 == 0:
        return (arr[size // 2] + arr[(size // 2) + 1]) / 2.0
    else:
        return arr[(size + 1) // 2]


def activityNotifications(expenditure, d):
    notifications = 0
    for index in range(len(expenditure) - d):
        notifications += int(expenditure[index + d] > median(expenditure[index:index + d]) * 2 - 1)
    return notifications


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)