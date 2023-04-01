def same_case(a: str, b: str):
    if a.isalpha() + b.isalpha() < 2:
        return -1
    if a.isupper() and b.isupper():
        return 1
    if a.islower() and b.islower():
        return 1
    else:
        return 0