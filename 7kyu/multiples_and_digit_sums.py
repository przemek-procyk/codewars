def procedure(i):
    sum_of_digits = []
    lista = list(range(i, 101,i))
    lista_str = [str(i) for i in lista]
    for i in lista_str:
        sum_of_digits.append(sum([int(j) for j in i]))
    return sum(sum_of_digits)


def procedure(i):
    multiplier = 1
    final_sum = 0
    multiple = i * multiplier
    while multiple <= 100:
        print(f"{multiplier} base {multiple}")
        final_sum += sum([int(i) for i in str(multiple)])
        multiplier += 1
        multiple = i * multiplier
    return final_sum


def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))