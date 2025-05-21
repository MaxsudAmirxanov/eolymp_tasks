from functools import lru_cache

@lru_cache(maxsize=None)
def f(m, n):
    if m == 0 or m == n:
        return 1
    return f(m - 1, n - 1) + f(m, n - 1)

m, n = map(int, input().split())
print(f(m, n))
