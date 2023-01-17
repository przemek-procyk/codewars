def is_odd_heavy(arr):
    if len(arr) == 0:
        return False
    try:
        even_elements = []
        odd_elements = []
        for i in arr:
            if i % 2 == 0:
                even_elements.append(i)
            else:
                odd_elements.append(i)
        odd_elements.sort()
        even_elements.sort(reverse=True)
        #return even_elements, odd_elements
        if len(even_elements) == 0:
            return True
        if len(odd_elements) == 0:
            return False
        for i in odd_elements:
            if i < even_elements[0]:
                return False
        return True
    except ValueError:
        return False


def is_odd_heavy(arr):
    try:
        min_odd = min(filter(lambda x: x % 2 != 0, arr))
    except:
        return False

    try:
        max_even = max(filter(lambda x: x % 2 == 0, arr))
    except:
        return True

    return min_odd - max_even > 0


def is_odd_heavy(arr):
    maxEven = max(filter(lambda n: n%2 == 0, arr), default=float("-inf"))
    minOdd  = min(filter(lambda n: n%2 == 1, arr), default=float("-inf"))
    return maxEven < minOdd