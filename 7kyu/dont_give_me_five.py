def dont_give_me_five(start,end):
    result = 0
    for i in range(start,end+1):
        if "5" in str(i):
            continue
        else:
            result +=1
    return result  # amount of numbers

a = ("....")
b = ("..")

print(a+b)