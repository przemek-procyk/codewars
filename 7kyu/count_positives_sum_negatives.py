def count_positives_sum_negatives(arr):
    if arr != []:
        negatives = 0
        positives = 0
        for number in arr:
            if number < 0:
                negatives += number
            if number > 0:
                positives += 1
        return [positives, negatives]
    else:
        return []

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
c = []
print(count_positives_sum_negatives(c))

print(c)

