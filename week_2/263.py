n = int(input())
count = 0
for i in range(1, n + 1):
    if bin(i).count('1') == 3:
        count += 1
print(count)
