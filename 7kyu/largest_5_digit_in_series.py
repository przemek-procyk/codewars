def solution(digits):
    maxi = 0
    for i in range(len(digits)):
        piece_5 = int(digits[i:i+5])
        if piece_5 > maxi:
            maxi = piece_5
    return maxi

print(solution('1234567898765'))