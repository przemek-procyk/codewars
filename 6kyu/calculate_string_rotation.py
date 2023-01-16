def shifted_diff(first, second):
    if len(first) == len(second):
        return (second + second).find(first)
    else:
        return -1
