def seven_ate9(str_):
    result = str_
    while "797" in result:
        result = result.replace("797", "77")
    return result

print((seven_ate9('797')))