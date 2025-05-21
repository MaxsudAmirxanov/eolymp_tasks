def count_ones(a, b):
    total = 0
    for i in range(a, b + 1):
        total += bin(i).count('1')
    return total

a, b = map(int, input().split())
print(count_ones(a, b))
