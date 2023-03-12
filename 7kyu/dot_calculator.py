# def calculator(txt):
#     dicto = {"add": " + ", "sub": " - ", "multi": " * ", "division": " // "}
#     if " * " in txt:
#         s = txt.split(dicto["multi"])
#         d = len(s[0]) * len(s[1])
#         b = ""
#         for i in range(1, d +1):
#             b += "."
#         return b
#     if " + " in txt:
#         s = txt.split(dicto["add"])
#         return s[0] + s[1]
#     if " - " in txt:
#         s = txt.split(dicto["sub"])
#         d = len(s[0]) - len(s[1])
#         b = ""
#         for i in range(1, d +1):
#             b += "."
#         return b
#     if " // " in txt:
#         s = txt.split(dicto["division"])
#         d = len(s[0]) // len(s[1])
#         b = ""
#         for i in range(1, d +1):
#             b += "."
#         return b
#
#
# #print(calculator(("..... + ...............")))
# print(calculator((". // ..")))
# print(calculator(("....... // ....")))
# # b = ""
# for i in range(1, 15 + 1):
#     b += "."
#
# print(b)
print(5//2)


def calculator(txt):
    a, op, b = txt.split()
    a, b = len(a), len(b)
    return '.' * eval(f'{a} {op} {b}'), a, op, b

print(calculator((". // ..")))