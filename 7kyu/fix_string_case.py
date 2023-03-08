def solve(s):
    lower_counter = 0
    upper_counter = 0
    for i in s:
        if i.islower():
            lower_counter +=1
        else:
            upper_counter +=1
    if lower_counter >= upper_counter:
        return s.lower()
    else:
        return s.upper()

print((solve("COde")))