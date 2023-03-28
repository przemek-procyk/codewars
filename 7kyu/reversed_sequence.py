def reverse_seq(n):
    list = []
    for i in range(n, 0, -1):
        list.append(i)

    return list


print(reverse_seq(5))


def reverse_seq(n):
    list = []
    for i in range(1,n + 1):
        list.append(i)

    return list[::-1]