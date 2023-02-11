def pillars(num_pill, dist, width):
    if num_pill < 2:
        return 0
    result = num_pill * ((dist * 100) + width) - (width * 2) - (dist * 100)
    return result


