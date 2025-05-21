n, m = map(int, input().split())
result = 0
for i in range(1, 100):
    result = (result + i * pow(i + 1, n, m)) % m
print(result)
