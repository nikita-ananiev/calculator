import math
import stack
funccountarg = {'power': 2, 'sin': 1, 'cos': 1, 'tg': 1, 'abs': 1, 'sqrt': 1, 'log': 2,
                'atg' : 1, 'asin' : 1, 'acos' : 1, 'C' : 2, 'A' : 2, 'P' : 1, 'pi' : 0,
                'e' : 0, 'hypot' : 2, 'ellipseArea' : 2, 'roundArea' : 1}

def factorial(arg):
    con = 1
    for i in range(1, int(arg) + 1):
        con *= i
    return con


def run0func(name):
    if name == 'pi':
        return math.pi
    elif name == 'e':
        return math.e


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
    elif name[0] == 'atg':
        return math.degrees(math.atan(arg))
    elif name[0] == 'asin':
        return math.degrees(math.asin(arg))
    elif name[0] == 'acos':
        return math.degrees(math.acos(arg))
    elif name[0] == 'P':
        return factorial(arg)
    elif name[0] == 'roundArea':
        return math.pi * arg**2


def run2func(name, a1, a2):
    if name == 'power':
        return math.pow(a1, a2)
    elif name == 'log':
        return math.log(a2, a1)
    elif name == 'C':
        return factorial(a2) / (factorial(a2 - a1) * factorial(a1))
    elif name == 'A':
        return factorial(a2) / factorial(a2 - a1)
    elif name == 'hypot':
        return math.hypot(a1, a2)
    elif name == 'ellipseArea':
        return math.pi * a1 * a2


def unr(x):
    return x * (-1)


def run(splexems):
    stack.clear()
    for i in splexems:
        if type(i) is float:
            stack.push(float(i))
        elif i in '+-*/^':
            a = stack.pop()
            b = stack.pop()
            if i == '+' : stack.push(b + a)
            elif i == '-' : stack.push(b - a)
            elif i == '*' : stack.push(a * b)
            elif i == '/' : stack.push(b / a)
            else: stack.push(math.pow(b, a))
        elif i == 'min':
            a = stack.pop()
            stack.push(unr(a))
        elif i == '!':
            a = stack.pop()
            stack.push(factorial(a))
        else:
            if funccountarg[i[1:]] == 1:
                a = stack.pop()
                stack.push(runfunc([i[1:]], a))
            elif funccountarg[i[1:]] == 2:
                a = stack.pop()
                b = stack.pop()
                stack.push(run2func(i[1:], b, a))
            else:
                stack.push(run0func(i[1:]))
    return stack.pop()