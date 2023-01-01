def zero_plentiful(arr):
    if 0 in arr:
        counter = 0
        zero_counter = 0
        for number in arr:
            if number == 0:
                zero_counter += 1
            else:
                if zero_counter >= 4:
                    counter += 1
                    zero_counter = 0
                else:
                    if zero_counter > 0:
                        return 0
        return counter
    return 0

