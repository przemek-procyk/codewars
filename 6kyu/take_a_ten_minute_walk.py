def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        if (walk.count("n") == walk.count("s")) and\
                (walk.count("w") == walk.count("e")):
            return True
        else:
            return False


def is_valid_walk(walk):
    n_s, e_w = 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == "n":
                n_s += 1
            elif i == "s":
                n_s -= 1
            elif i == "w":
                e_w += 1
            elif i == "e":
                e_w -= 1
    else:
        return False
    return n_s == 0 and e_w == 0

def is_valid_walk(walk):
    start = [0, 0]
    current = [0, 0]
    moves_dict = {"n": (lambda curr: [curr[0], curr[1] + 1]), "s": (lambda curr: [curr[0], curr[1] - 1]),
                  "e": (lambda curr: [curr[0] + 1, curr[1]]), "w": (lambda curr: [curr[0] - 1, curr[1]])}
    if len(walk) == 10:
        for i in walk:
            current = moves_dict[i](current)
            print(moves_dict[i](current))
            print(f"C{current}")
        return start == current
    else:
        return False
