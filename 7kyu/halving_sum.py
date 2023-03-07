def halving_sum(n):
    total = [n]

    while n > 1:
        n = n // 2
        total.append(n)

    return sum(total)

print(halving_sum(25))