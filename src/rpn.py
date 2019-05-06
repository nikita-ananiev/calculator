import stack

prioritet = {',': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, 'min': 4}

def buildRPN(lexemes):
    spLexems = []
    i = 0
    lastlexem = ''
    flag = False
    for lexem in lexemes:
        i += 1
        if lexem[0] == 'F':
            lastlexem = lexem[0]
            stack.push(lexem)
            continue
        elif lexem[0] == 'N':
            lastlexem = lexem[0]
            spLexems.append(float(lexem[1:]))
            continue
        elif lexem[0] == ')':
            lastlexem = lexem[0]
            while not stack.empty():
                if stack.peek() == '(':
                    break
                else:
                    spLexems.append(stack.pop())
            stack.pop()
            continue
        elif lexem[0] == '(':
            stack.push('(')
            lastlexem = lexem[0]
            continue
        elif lexem[0] in '!':
            spLexems.append(lexem[0])
        elif lexem[0] == ',':
            j = stack.peek()
            while j != '(':
                spLexems.append(stack.pop())
                j = stack.peek()
            lastlexem = lexem[0]
        else:
            operation = lexem[0]
            if i == 1 or lastlexem in '(,^':
                if operation == '-':
                    operation = 'min'
                stack.push(operation)
                continue
            while not stack.empty():
                stackTop = stack.peek()
                if stackTop == '(':
                    break
                if stackTop[0] == 'F':
                    spLexems.append(stack.pop())
                    continue
                stackTopPriority = prioritet[stackTop]
                operationPriority = prioritet[operation]
                if (stackTopPriority > operationPriority):
                    spLexems.append(stack.pop())
                    continue
                if ((stackTopPriority == operationPriority) and (stackTop in '+-*/')):
                    spLexems.append(stack.pop())
                    continue
                break
            stack.push(operation)
            lastlexem = lexem[0]
    while not stack.empty():
        spLexems.append(stack.pop())
    return spLexems
