class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

# Пример использования
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.top())  # Вывод: 10
stack.pop()
print(stack.top())  # Вывод: 5
