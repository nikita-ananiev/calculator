import run
import rpn
import lexeme

#print(run.run(rpn.buildRPN(lexeme.lexemes('   1001 * sqrj(  9) '))))
print(run.run(rpn.buildRPN(lexeme.lexemes(input()))))
