def last_digit(n1, n2):
    if n1 == 0 and n2 == 0:
        return 1
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0

    if n2 % 4 == 0:
        rs = 4
    else:
        rs = n2 % 4

    number = pow(n1, rs)
    return number % 10


#----------------------------!
def last_digit(n1, n2):
    return pow( n1, n2, 10 )