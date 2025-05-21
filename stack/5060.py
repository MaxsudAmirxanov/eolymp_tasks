def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))  # Используем int() для округления вниз
        else:
            stack.append(int(token))
    return stack[0]

# Пример использования
tokens = ["2", "1", "+", "3", "*"]
print(eval_rpn(tokens))  # Вывод: 9
