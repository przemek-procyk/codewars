def high_and_low(numbers):
    list_str = sorted(numbers.split(), key=int)
    lista_int = [int(i) for i in list_str]
    return f"{max(lista_int)} {min(lista_int)}"


print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 9 3 4 -5"))

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))


print(max("1 9 3 4 -5"), key=int)