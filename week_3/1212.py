import math

total = 1
while True:
    try:
        n = int(input())
        total *= n
    except EOFError:
        break
print(total)
