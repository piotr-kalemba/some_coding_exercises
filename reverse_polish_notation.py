from collections import deque

def compute_rpn(string):
    stack = deque()
    terms = string.split()
    for term in terms:
        if term == '+':
            stack.append(stack.pop() + stack.pop())
        elif term == '*':
            stack.append(stack.pop() * stack.pop())
        elif term == '-':
            value_1 = stack.pop()
            stack.append(stack.pop() - value_1)
        elif term == '/':
            value_1 = stack.pop()
            if value_1 == 0:
                return None
            stack.append(stack.pop() / value_1)
        else:
            stack.append(float(term))

    result = stack.pop()
    return result

print(compute_rpn("2 3 7 4 + 5 2 - / * +"))
print(compute_rpn("2 0 /"))