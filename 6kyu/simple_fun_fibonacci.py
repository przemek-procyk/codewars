def find(a, b, n):
    """
    too slow for big tests
    """
    if a == 0 and b == 0:
        return 0
    fibo = str(a) + str(b)
    while len(fibo) <= n:
        a = fibo[-2]
        b = fibo[-1]
        c = a + b
        if c == 11:
            fibo = "1123581347"
            break
        if c == 14:
            fibo = "1459"
            break
        fibo += str(int(fibo[-1]) + int(fibo[-2]))

    return int(fibo[n])


def find2(a, b, n):
    if a + b == 0:
        return 0
    seq = [a, b]
    s = ""
    x = n
    while len(seq) <= n:
        a = seq[-2]
        b = seq[-1]
        c = a + b
        if c == 11:
            s = "1123581347"
            break
        if c == 14:
            s = "1459"
            break
        if c > 9:
            seq.append(c // 10)
        seq.append(c % 10)
    l = len(seq)
    return seq[n] if n < l else int(s[(n - l) % len(s)])
