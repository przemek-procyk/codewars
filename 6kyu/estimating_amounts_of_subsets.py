
def est_subsets(arr):
    # works but its too slow 
    if arr == []:
        return 0
    power_list = [[]]
    for element in set(arr):
        for sub_set in power_list:
            power_list = power_list + [list(sub_set)+[element]]

    b = [{x for x in power_list[i]} for i in range(1, len(power_list))]

    return len(b)


print(est_subsets([-41, 18, 6, 29, 41, 35, -18, 11, -50, 24, 8, 39, -34, -3, 17, 22, -13, 1, -10, 43, -26, 48, 45, -5, 14, 28, -23, 19, -37, -22, 13, 47, -45, -24, -7, 20, 15, -47, 42, -48, -35, -42, -38, -1, -21, 0, -28, -4, -46, -31, -19, -27, -29, -33, -32, 38, 27, 2, -12, 9, 16, -39, 31, -25, 21, -36, -30, -16, -6, -11, -14, 3, 12, 25, -40, 4, 36, -17, 26, 32, -49, -43, 23, 10, 7, 34]))



# def est_subsets(arr):
#     return 2**len(set(arr)) - 1


# arr = [2, 3, 4, 5, 5, 6, 6, 7, 8, 8]

# print(len(set(arr))-1) 