def clear_digits(n):
    count = [0] * 10
    for digit in str(n):
        count[int(digit)] += 1
    result = ''.join(digit for digit in str(n) if count[int(digit)] == 1)
    return result

n = int(input())
print(clear_digits(n))
