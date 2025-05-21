n = input().strip()
prod = 1
for digit in n:
    prod *= int(digit)
print(prod)
