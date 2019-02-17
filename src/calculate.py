import run
import rpn
import lexeme

def calculate(expression):
    return run.run(rpn.buildRPN(lexeme.lexemes(expression)))