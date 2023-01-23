def name(strings):
    values = {chr(i): val + 1 for val, i in enumerate(range(ord("a"), ord("z") + 1))}
    sum_of_values = [[values.get(i) for i in strings[n]] for n in range(0, len(strings))]
    test = [(len(i), sum(i)) for i in sum_of_values]

    return test
