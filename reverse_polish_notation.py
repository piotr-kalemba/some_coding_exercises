from collections import deque

def compute_rpn(r_p_n):
    stack = deque()
    terms = r_p_n.split()
    for term in terms:
        try:
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
        except Exception:
            print("Invalid Input Expression")
            return None

    return stack.pop()

print(compute_rpn("2 3 7 4 + 5 2 - / * +"))
print(compute_rpn("2 + 2 /"))