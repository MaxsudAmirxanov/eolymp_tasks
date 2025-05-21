import math

while True:
    i = int(input())
    if i == -1:
        break
    print(f"sqrt({i}) = {math.sqrt(i):.4f}")
    print(f"log({i}) = {math.log(i):.4f}")
    print(f"sin({i}) = {math.sin(i):.4f}")
