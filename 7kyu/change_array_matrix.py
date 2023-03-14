def matrix(array):
    for i in range(len(array)):
        if array[i][i] < 0:
            array[i][i] = 0
        else:
            array[i][i] = 1
    return array

c = [[-1, 4, -5, -9, 3],
     [6, -4, -7, 4, -5],
     [3, 5, 4, -9, -1],
     [1, 5, -7, -8, -9],
     [-3, 2, 1, -5, 6]]

print(matrix(c))
