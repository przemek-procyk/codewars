def longest_slide_down(pyramid):
    sum_slide = [[0 for j in range(len(pyramid[i]))] for i in range(len(pyramid))]
    sum_slide[0][0] = pyramid[0][0]
    for os_y, l in enumerate(pyramid, 0):
        for os_x in range(os_y + 1):
            if not os_x:
                sum_slide[os_y][os_x] = max(sum_slide[os_y][os_x], sum_slide[os_y - 1][os_x] + l[os_x])
            elif os_x < os_y:
                sum_slide[os_y][os_x] = max(sum_slide[os_y][os_x], sum_slide[os_y - 1][os_x] + l[os_x],
                                            sum_slide[os_y - 1][os_x - 1] + l[os_x])
            else:
                sum_slide[os_y][os_x] = max(sum_slide[os_y][os_x], sum_slide[os_y - 1][os_x - 1] + l[os_x])
    return max(sum_slide[:][-1])