def last_non_zero_digit(n):
    while n % 10 == 0:
        n //= 10
    return n % 10

n = int(input())
print(last_non_zero_digit(n))
