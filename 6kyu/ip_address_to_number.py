from textwrap import wrap


def ip_to_num(ip: str):
    binaries = int(("".join([bin(int(i))[2:].zfill(8) for i in ip.split(".")])), 2)

    return binaries


def num_to_ip(num):
    num_to_bin = bin(num)[2:].zfill(32)
    b = wrap(num_to_bin, 8)
    c = [int(i, 2) for i in b]
    return ".".join(str(i) for i in c)
