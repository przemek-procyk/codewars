def sort_array(source_array):
    odd_array = sorted([number for number in source_array if number % 2 != 0])
    sorted_array = []
    odd_array_index = 0

    for number in source_array:
        if number in odd_array:
            sorted_array.append(odd_array[odd_array_index])
            odd_array_index += 1
        else:
            sorted_array.append(number)

    return sorted_array



def sort_array2(source_array):
    odd = sorted([number for number in source_array if number % 2 != 0])
    return [number if number % 2 == 0 else odd.pop(0) for number in source_array]


