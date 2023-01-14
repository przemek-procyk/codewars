def solve(arr):
    arr = sorted(arr)
    if arr[0] + arr[1] <= arr[2]:
        return arr[0] + arr[1]
    else:
        return sum(arr) // 2



