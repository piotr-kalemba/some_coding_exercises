from collections import deque

def valid_rpn(r_p_n):
    stack = deque()
    terms = r_p_n.split()
    try:
        for term in terms:
            if term in {'+', '*', '-', '/'}:
                stack.pop()
            else:
                stack.append(float(term))
        stack.pop()
        if stack:
            return False
    except Exception:
        return False
    return True

def compute_rpn(r_p_n):
    stack = deque()
    terms = r_p_n.split()
    if not valid_rpn(r_p_n):
        print('Invalid input')
        return None
    try:
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
                    stack.append(stack.pop() / value_1)
                else:
                    stack.append(float(term))
    except ZeroDivisionError:
        print("Zero Division Error")
        return None

    return stack.pop()

def rpn_to_nn(r_p_n):
    stack = deque()
    terms = r_p_n.split()
    if not valid_rpn(r_p_n):
        print('Invalid input')
        return None

    for term in terms:
        if term == '+':
            value_1 = stack.pop()
            stack.append(f'({stack.pop()} + {value_1})')
        elif term == '*':
            value_1 = stack.pop()
            stack.append(f'({stack.pop()} * {value_1})')
        elif term == '-':
            value_1 = stack.pop()
            stack.append(f'({stack.pop()} - {value_1})')
        elif term == '/':
            value_1 = stack.pop()
            stack.append(f'({stack.pop()} / {value_1})')
        else:
            stack.append(str(term))

    return stack.pop()[1:-1]


nn = rpn_to_nn('2 3 7 4 + 5 2 - / * +')
print(nn)
nn = rpn_to_nn('2 2 + 3 3 + 4 4 + * /')
print(nn)
f = valid_rpn('1 1 1 +')
print(f)

