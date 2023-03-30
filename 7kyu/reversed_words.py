def reverse_words(s):
    words = s.split(' ')
    new_s = ' '.join(reversed(words))
    return new_s

b = "Roman kocha hirołsy"

print(reverse_words(b))