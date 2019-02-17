import math
import stack
funccountarg = {'power': 2, 'sin': 1, 'cos': 1, 'tg': 1, 'abs': 1, 'sqrt': 1, 'log': 2}

def runfunc(name, arg):
    if name[0] == 'abs':
        return abs(arg)
    elif name[0] == 'sqrt':
        return math.sqrt(arg)
    elif name[0] == 'sin':
        arg = arg * math.pi / 180
        return math.sin(arg)
    elif name[0] == 'cos':
        arg = arg * math.pi / 180
        return math.cos(arg)
    elif name[0] == 'tg':
        arg = arg * math.pi / 180
        return math.tan(arg)

def run2func(name, a1, a2):
    if name == 'power':
        return math.pow(a1, a2)
    if name == 'log':
        return math.log(a2, a1)

def unr(x):
    return x * (-1)

def run(splexems):
    stack.clear()
    for i in splexems:
        if type(i) is float:
            stack.push(float(i))
        elif i in '+-*/':
            a = stack.pop()
            b = stack.pop()
            if i == '+' : stack.push(b + a)
            elif i == '-' : stack.push(b - a)
            elif i == '*' : stack.push(a * b)
            else: stack.push(b / a)
        elif i == 'min':
            a = stack.pop()
            stack.push(unr(a))
        else:
            if funccountarg[i[1:]] == 1:
                a = stack.pop()
                stack.push(runfunc([i[1:]], a))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.push(run2func(i[1:], b, a))
    return stack.pop()