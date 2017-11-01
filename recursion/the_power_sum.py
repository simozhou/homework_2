X, N = int(input()), int(input())


def power_sum(total, power, number=1):
    value = int(total - number ** power)
    # fail case
    if value < 0:
        return 0
    # success case
    elif value == 0:
        return 1
    # recursive step
    else:
        return power_sum(value, power, number + 1) + power_sum(total, power, number + 1)


print(power_sum(X, N))
