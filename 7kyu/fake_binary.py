def fake_bin(x):
    str = ""
    for i in x:
        if i >= "5":
            str += "1"
        else:
            str += "0"
    return str

print(fake_bin('509321967506747'))