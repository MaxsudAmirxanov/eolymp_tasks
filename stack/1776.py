def can_reorder(arrivals, departures):
    stack = []
    i = 0
    for train in departures:
        while i < len(arrivals) and arrivals[i] != train:
            stack.append(arrivals[i])
            i += 1
        if i < len(arrivals) and arrivals[i] == train:
            i += 1
        elif stack and stack[-1] == train:
            stack.pop()
        else:
            return False
    return True

# Пример использования
arrivals = [1, 2, 3, 4, 5]
departures = [4, 5, 3, 2, 1]
print(can_reorder(arrivals, departures))  # Вывод: True
