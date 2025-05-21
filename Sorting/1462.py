n = int(input())
def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

count = sum(1 for i in range(1, n + 1) if is_prime(i))
print(count)
