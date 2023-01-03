def count_nines2(n):
    """
    too slow for bigger numbers
    """
    print(n)
    nine_counter = 0
    for i in range(0, n + 1):
        nine_counter += str(i).count('9')
    return nine_counter


def count_nines(n):
    nine_counter = 0
    number_list = [i for i in str(n)]
    while len(number_list) > 0:
        if len(number_list) == 1:
            if number_list[0] == '9':
                nine_counter += 1
        else:
            nine_counter += int(number_list[0]) * int(str(len(number_list)-1) + '0' * (len(number_list)-2))
            if number_list[0] == '9':
                nine_counter += int(''.join(number_list[1:]))+1
        number_list.pop(0)

    return nine_counter

