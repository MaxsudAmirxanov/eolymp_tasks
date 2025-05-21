class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Пример использования
min_stack = MinStack()
min_stack.push(10)
min_stack.push(20)
print(min_stack.get_min())  # Вывод: 10
min_stack.pop()
print(min_stack.get_min())  # Вывод: 10
