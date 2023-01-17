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


print(is_odd_heavy([0, 2, 19, 4, 4]))

print(is_odd_heavy([11, 4, 9, 2, 3, 10]))

print(is_odd_heavy([11, 4, 9, 2, 8]))

print(is_odd_heavy([0, 0, 0, 0, 0]))

print(is_odd_heavy([1,-2,-1,2]))

print(is_odd_heavy([1]))


def isOddHeavy(arr):
    try:
        min_odd = min(filter(lambda x: x % 2 != 0, arr))
    except:
        return False

    try:
        max_even = max(filter(lambda x: x % 2 == 0, arr))
    except:
        return True

    return min_odd - max_even > 0


def isOddHeavy(arr):
    maxEven = max(filter(lambda n: n%2 == 0, arr), default=float("-inf"))
    minOdd  = min(filter(lambda n: n%2 == 1, arr), default=float("-inf"))
    return maxEven < minOdd