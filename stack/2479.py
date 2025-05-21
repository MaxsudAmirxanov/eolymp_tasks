def is_balanced(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs.get(stack.pop()) != char:
                return False
    return not stack

# Пример использования
s = "{[()]}"
print(is_balanced(s))  # Вывод: True
