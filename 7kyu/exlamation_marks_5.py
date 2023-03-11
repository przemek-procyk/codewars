def remove(s:str):
    c = s.split()
    result = " ".join([i.rstrip("!") for i in c])
    return result

print(remove('Hi! Hi!'))
# print(remove('!!!Hi !!hi!!! !hi'))