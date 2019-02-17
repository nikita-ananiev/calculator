import run
import rpn
import lexeme

#print(run.run(rpn.buildRPN(lexeme.lexemes('   1001 * sqrj(  9) '))))
print(run.run(rpn.buildRPN(lexeme.lexemes(input()))))

#while True:
    #expression = input('Please type an expression (or press ENTER for exit): ')
    #if len(expression) == 0:
        #break
    #lexemes = lexeme.lexemes(expression)
    #print(lexemes)
    #rpnLexemes = rpn.buildRPN(lexemes)
    #print(rpnLexemes)
    #result = run.run(rpnLexemes)
    #print(result)

