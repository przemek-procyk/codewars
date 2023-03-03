def kooka_counter(laughing):
    l = []
    birds = 0
    if laughing == "":
        return 0
    else:
        for i in laughing:
            if i != "a":
                l.append(i)
        for i in range(1, len(l)):
            if l[i] != l[i-1]:
                birds +=1
    return birds + 1
