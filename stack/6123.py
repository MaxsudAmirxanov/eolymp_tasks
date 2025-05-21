class SafeStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print("Ошибка: попытка извлечь элемент из пустого стека")

    def top(self):
        if self.stack:
            return self.stack[-1]
        print("Ошибка: стек пуст")
        return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

# Пример использования
safe_stack = SafeStack()
safe_stack.pop()  # Вывод: Ошибка: попытка извлечь элемент из пустого стека
