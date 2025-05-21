from math import gcd
numbers = list(map(int, input().split()))
total = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        total += gcd(numbers[i], numbers[j])
print(total)
