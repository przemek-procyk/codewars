def is_palindrome(s):
    new_s = s.lower()
    return new_s == new_s[::-1]

