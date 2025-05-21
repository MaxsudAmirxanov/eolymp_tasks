from collections import deque

def min_knight_moves(start, end):
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == end:
            return moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    return -1

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
print(min_knight_moves(start, end))
