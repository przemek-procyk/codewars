def diamond(n):
    if n < 1 or not n % 2:
        return None
    mid = n // 2
    string = ''
    for i in range(int(n/2)):
        string += " " * (mid - i) + "*" * (2*i +1) + "\n"
    for i in range(int(n/2),-1,-1):
        string += (mid-i) * " " + (2*i+1) * "*" + '\n'
    return string
print(diamond(9))
