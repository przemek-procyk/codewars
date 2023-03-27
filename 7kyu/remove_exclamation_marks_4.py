import re

#
# def remove(s):
#     new_s = s.strip("!")
#     new_s += ("!")
#     return new_s
#
#
# b = "Hi! Hi!"
#
# print(remove(b))

import re
def remove(s):
    new_s = re.sub('!', "", s)
    new_s += ("!")
    return new_s

b = "Hi! Hi!"

print(remove(b))


def remove(s: str):
    result = s.replace("!", "") + "!"
    return result