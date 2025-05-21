n = input()
count = 0
for digit in n:
    count += 1
    if digit == '5':
        break
print(count)
