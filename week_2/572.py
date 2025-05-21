n = int(input())
divisors = set()
for i in range(2, int(n**0.5) + 1):
    while n % i == 0:
        divisors.add(i)
        n //= i
if n > 1:
    divisors.add(n)
print(len(divisors))
