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
    except IndexError:
        return False
    except ValueError:
        return False
    return True


def evaluate_rpn(r_p_n):
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


def space_out(n_n):

    indices_to_replace = [index for index in range(len(n_n)) if n_n[index] in {'(', ')', '+', '*','-','/'}]
    for index in indices_to_replace:
        if n_n[index] == '(':
            n_n[index] = '( '
        elif n_n[index] == ')':
            n_n[index] = ' )'
        else:
            n_n[index] = f' {n_n[index]} '
    return ''.join(n_n)


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
    if brackets_number(nn) != operations_number(nn):
        nn = f' {nn} '
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
        return evaluate_rpn(r_p_n)


if __name__ == '__main__':
    nn = rpn_to_nn('2 3 7 4 + 5 2 - / * +')
    print(nn)
    nn = rpn_to_nn('2 2 + 3 3 + 4 4 + * /')
    print(nn)
    f = valid_rpn('1 1 1 +')
    print(f)
