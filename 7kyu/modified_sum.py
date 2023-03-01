def modified_sum(a, n):
    sum_o = 0
    for i in a:
        sum_o += i ** n
    return sum_o - sum(a)


print(modified_sum([1, 2, 3], 3))
