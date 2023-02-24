def shorter_reverse_longer(a,b):
    if len(a) < len(b):
        return f'{a}{b[::-1]}{a}'
    else:
        return f'{b}{a[::-1]}{b}'