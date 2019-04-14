def lexemes(phrase):
    lex = []
    flag1 = False
    for i in range(len(phrase)):
        if flag1:
            if i != j:
                continue
            flag1 = False
        if phrase[i] in 'ACPabcdefghijklmnopqrstuvwxyz_':
            lexem = ''
            j = i
            flag1 = True
            while phrase[j] in 'ACPabcdefghijklmnopqrstuvwxyz_':
                lexem += phrase[j]
                j += 1
                if j == len(phrase):
                    break
            lexem = list(lexem)
            lexem.insert(0, 'F')
            lexem = ''.join(lexem)
            lex.append(lexem)
            lexem = ''
        elif phrase[i] in '.0123456789':
            lexem = ''
            j = i
            flag1 = True
            while phrase[j] in '.0123456789':
                lexem += phrase[j]
                j += 1
                if j == len(phrase):
                    break
            lexem = list(lexem)
            lexem.insert(0, 'N')
            lexem = ''.join(lexem)
            lex.append(lexem)
            lexem = ''
        elif phrase[i] in '+-/*()^!,':
            lex.append(phrase[i])
    return lex
