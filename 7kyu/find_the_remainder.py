def remainder(a, b):
    if min(a, b) != 0:
        return max(a, b) % min(a, b)


print(remainder(0, 12))
