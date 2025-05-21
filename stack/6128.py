from collections import deque

d = deque()
d.append(1)  # Добавить в конец
d.appendleft(2)  # Добавить в начало
print(d)  # Вывод: deque([2, 1])
d.pop()  # Удалить с конца
d.popleft()  # Удалить с начала
print(d)  # Вывод: deque([])
