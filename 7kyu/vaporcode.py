def vaporcode(s: str):
    return "  ".join(i.upper() for i in s if i != " ")


# print(vaporcode("Lets go to the movies"))



d = ("Lets go to the movies")

def vaporcode2(s):
    stra = ""
    for i in s:
        if i != " ":
            stra += i.upper()
    return "  ".join(stra)


print(vaporcode2(("Lets go to the movies")))
