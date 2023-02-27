def get_larger_numbers(a, b):
    new_list = []
    for i in range(0, len(a)):
        if a[i] > b[i]:
            new_list.append(a[i])
        else:
            new_list.append(b[i])
    return new_list