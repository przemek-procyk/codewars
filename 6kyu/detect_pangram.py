def is_pangram(s):
    s_lower = s.lower()
    counter = 0
    for i in range(97, 123):
        if chr(i) in s_lower:
            counter +=1
    return True if counter >= 26 else False

