while True:
    n = int(input())
    if n == 0:
        break
    sequence = []
    for _ in range(n):
        sequence.append(int(input()))
    stack = []
    current = 1
    possible = True
    for num in sequence:
        while stack and stack[-1] == current:
            stack.pop()
            current += 1
        if num == current:
            current += 1
        else:
            stack.append(num)
    while stack and stack[-1] == current:
        stack.pop()
        current += 1
    if not stack:
        print("yes")
    else:
        print("no")
