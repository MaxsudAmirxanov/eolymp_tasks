def min_thread_length(n, positions):
    positions.sort()
    length = 0
    for i in range(1, n):
        length += positions[i] - positions[i - 1]
    return length

n = int(input())
positions = list(map(int, input().split()))
print(min_thread_length(n, positions))
