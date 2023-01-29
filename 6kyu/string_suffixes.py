def string_suffix(str_):
    work_str = list(str_)
    dupnik_licznik = 0

    while len(work_str) > 0:
        suffixes_sum = 0
        for idx, val in enumerate(work_str):
            if val == str_[idx]:
                suffixes_sum += 1
            else:
                break
        work_str.pop(0)
        dupnik_licznik += suffixes_sum

    return dupnik_licznik
