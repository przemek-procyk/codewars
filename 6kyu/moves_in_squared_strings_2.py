def rot(strng):
    return r'\n'.join([i[::-1] for i in strng.split(r'\n')[::-1]])


def selfie_and_rot(strng):
    b = [i + len(i) * "." for i in strng.split("\n")]
    k = '\n'.join(b) + ("\n" + rot('\n'.join(b)))
    return k


def oper(fct, s):
    return fct(s)
