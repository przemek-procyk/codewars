def abbrev_name(name):
    new_name = name.split(" ")
    abbrev = ".".join(new_name[0][0].upper() + new_name[1][0].upper())
    return abbrev
