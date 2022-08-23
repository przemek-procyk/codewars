def increment_string(strng:str):
    without_ints = strng.rstrip("1234567890")
    ints = strng[len(without_ints):]
    if len(ints) == 0:
        return strng + "1"
    else:
        return without_ints + str(int(ints) + 1).zfill(len(ints))
