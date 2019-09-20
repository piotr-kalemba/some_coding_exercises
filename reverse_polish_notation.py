from collections import deque


def space_out(expr):
    expr = list(expr)
    indices_to_replace = [index for index in range(len(expr)) if expr[index] in {'(', ')', '+', '*','-','/'}]
    for index in indices_to_replace:
        if expr[index] == '(':
            expr[index] = '( '
        elif expr[index] == ')':
            expr[index] = ' )'
        else:
            expr[index] = f' {expr[index]} '
    return ''.join(expr)


def valid_rpn(r_p_n):
    stack = deque()
    r_p_n = space_out(r_p_n)
    terms = r_p_n.split()
    try:
        for term in terms:
            if term in {'+', '*', '-', '/'}:
                stack.pop()
                if not stack:
                    return False
            else:
                stack.append(float(term))
        stack.pop()
        if stack:
            return False
    except IndexError:
        return False
    except ValueError:
        return False
    return True


def evaluate_rpn(r_p_n):
    stack = deque()
    r_p_n = space_out(r_p_n)
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
    r_p_n = space_out(r_p_n)
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


def brackets_number(expr):
    return expr.count('(')


def operations_number(expr):
    return expr.count('+') + expr.count('-') + expr.count('*') + expr.count('/')


def valid_nn(n_n):
    stack = deque()
    nn = space_out(n_n)
    if brackets_number(n_n) != operations_number(n_n):
        nn = f'( {nn} )'
    terms = nn.split()
    try:
        for term in terms:
            if term == ')':
                stack.pop()
                term_1 = stack.pop()
                if term_1 != '#':
                    return False
                stack.pop()
                term_2 = stack.pop()
                if term_2 != '(':
                    return False
                stack.append('term')
            elif term == '(':
                stack.append('(')
            elif term in {'+', '*', '-', '/'}:
                stack.append('#')
            else:
                stack.append(float(term))
        last = stack.pop()
        if last != 'term':
            return False
        if stack:
            return False
    except IndexError:
        return False
    except ValueError:
        return False
    return True


def nn_to_rpn(n_n):
    stack = deque()
    if not valid_nn(n_n):
        print("Invalid input!")
        return None
    nn = space_out(n_n)
    if brackets_number(nn) == operations_number(nn) - 1:
        nn = f'( {nn} )'
    terms = nn.split()
    for term in terms:
        if term == '(':
            continue
        elif term == ')':
            term_1 = stack.pop()
            term_2 = stack.pop()
            term_3 = stack.pop()
            stack.append(f'{term_3} {term_1} {term_2}')
        else:
            stack.append(str(term))
    return stack.pop()


def evaluate_nn(n_n):
    r_p_n = nn_to_rpn(n_n)
    if r_p_n:
        try:
            return evaluate_rpn(r_p_n)
        except ZeroDivisionError:
            print("Zero Division Error!")
            return None


