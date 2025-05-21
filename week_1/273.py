x, n, m = map(int, input().split())

def mod_pow(x, n, m):
    result = 1
    x = x % m
    while n > 0:
        if n % 2 == 1:
            result = (result * x) % m
        x = (x * x) % m
        n //= 2
    return result

print(mod_pow(x, n, m))
