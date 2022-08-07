def remainder(a, b):
    if a > b:
        if b == 0:
            return None
        else:
            return a % b
    if b > a:
        if a == 0:
            return None
        else:
            return b % a
    if a == 0 and b == 0:
        return None

    if a == b:
        return 0