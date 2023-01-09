from functools import lru_cache


def fibonacci(n):
    def fib_memo(n, m):
        if n in m:
            return m[n]
        answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
        m[n] = answer
        return answer

    m = {1: 1, 2: 1}
    return fib_memo(n, m)


@lru_cache(maxsize=1000)
def fibonacci2(input_value):
    if input_value == 1:
        return 1
    elif input_value == 2:
        return 1
    elif input_value > 2:
        return fibonacci(input_value - 1) + fibonacci(input_value - 2)
