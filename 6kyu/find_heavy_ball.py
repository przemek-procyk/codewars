def find_ball(scales):
    w = scales.get_weight([0, 1, 2, 3], [4, 5, 6, 7])
    if w < 0:
        w = scales.get_weight([0, 1], [2, 3])
        if w < 0:
            w = scales.get_weight([0], [1])
            return 0 if w < 0 else 1
        else:
            w = scales.get_weight([2], [3])
            return 2 if w < 0 else 3
    else:
        w = scales.get_weight([4, 5], [6, 7])
        if w < 0:
            w = scales.get_weight([4], [5])
            return 4 if w < 0 else 5
        else:
            w = scales.get_weight([6], [7])
            return 6 if w < 0 else 7

    return -1
