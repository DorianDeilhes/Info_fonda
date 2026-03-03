from arithmetic_expressions import (DivExpr, Litteral, MulExpr, SubExpr, AddExpr, OppExpr, Variable, Assignment)
from arithmetic_lexer import tokens
from ply import yacc

# Assignment level (lowest precedence)
def p_expression_assignment(p):
    'expression : IDENTIFIER ASSIGN expression'
    p[0] = Assignment(p[1], p[3])

# Expression level (+ and -)
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = AddExpr(p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = SubExpr(p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# Term level (higher precedence: * and /)
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = MulExpr(p[1], p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = DivExpr(p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# Factor level (highest precedence: numbers, variables, parentheses, and unary minus)
def p_factor_number(p):
    'factor : NUMBER'
    p[0] = Litteral(float(p[1]))

def p_factor_identifier(p):
    'factor : IDENTIFIER'
    p[0] = Variable(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_unary_minus(p):
    'factor : MINUS factor'
    p[0] = OppExpr(p[2])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")
    

parser = yacc.yacc()

if __name__ == "__main__":
    print(parser.parse('42').eval())
    print(parser.parse('((2 + 7)*(4-2))').eval())
    print(str(parser.parse('(2+(3*1))')))
    print(parser.parse('(2+(3*1))'))
    print(parser.parse('(2+(3*1))').eval())
    
    # New tests: expressions without unnecessary parentheses
    print("\n--- Tests without parentheses ---")
    print(f"2+3*4 = {parser.parse('2+3*4').eval()}")
    print(f"4/2*3 = {parser.parse('4/2*3').eval()}")
    print(f"4-2-2 = {parser.parse('4-2-2').eval()}")
    print(f"10-3+2 = {parser.parse('10-3+2').eval()}")
    print(f"2*3+4*5 = {parser.parse('2*3+4*5').eval()}")
    print(f"str(2+3*4) = {str(parser.parse('2+3*4'))}")
    
    # Tests for negative numbers (unary minus)
    print("\n--- Tests with negative numbers ---")
    print(f"-4 = {parser.parse('-4').eval()}")
    print(f"--4 = {parser.parse('--4').eval()}")
    print(f"3 + -4 = {parser.parse('3 + -4').eval()}")
    print(f"-(4*2) = {parser.parse('-(4*2)').eval()}")
    print(f"3 + -(--4*2) = {parser.parse('3 + -(--4*2)').eval()}")
    print(f"str(3+-4) = {str(parser.parse('3+-4'))}")
    
    # Tests for variables
    print("\n--- Tests with variables ---")
    env = {'x': 5, 'y': 3, 'abc': 10}
    print(f"x (with x=5) = {parser.parse('x').eval(env)}")
    print(f"3+x (with x=5) = {parser.parse('3+x').eval(env)}")
    print(f"x*y (with x=5, y=3) = {parser.parse('x*y').eval(env)}")
    print(f"2*x+y (with x=5, y=3) = {parser.parse('2*x+y').eval(env)}")
    print(f"abc-x (with abc=10, x=5) = {parser.parse('abc-x').eval(env)}")
    print(f"str(3+x) = {str(parser.parse('3+x'))}")
    
    # Tests for assignments
    print("\n--- Tests with assignments ---")
    env2 = {}  # Fresh environment
    print(f"a <- 10 = {parser.parse('a <- 10').eval(env2)}")  # Returns 10 and sets a
    print(f"After assignment, a = {env2['a']}")  # Check environment
    print(f"b <- a * 2 = {parser.parse('b <- a * 2').eval(env2)}")  # b = 20
    print(f"c <- a + b = {parser.parse('c <- a + b').eval(env2)}")  # c = 30
    print(f"Environment now: {env2}")  # Show all variables
    print(f"str(x <- 5+3) = {str(parser.parse('x <- 5+3'))}")  # Show tree structure



# ancienne version du parser, avec des règles plus simples, mais qui nécessitent des parenthèses partout.

""" def p_litteral(p) :
    'expression : NUMBER'
    p[0] = Litteral(int(p[1]))

def p_expression_add(p):
    'expression : LPAREN expression PLUS expression RPAREN'
    p[0] = AddExpr(p[2], p[4])

def p_expression_sub(p):
    'expression : LPAREN expression MINUS expression RPAREN'
    p[0] = SubExpr(p[2], p[4])

def p_expression_mul(p):
    'expression : LPAREN expression TIMES expression RPAREN'
    p[0] = MulExpr(p[2], p[4])

def p_expression_div(p):
    'expression : LPAREN expression DIVIDE expression RPAREN'
    p[0] = DivExpr(p[2], p[4])




def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = AddExpr(p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = MulExpr(p[1], p[3])

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = Litteral(int(p[1]))

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]




def p_error(p):
    print(f"Syntax error at '{p.value}'")
    

parser = yacc.yacc()

if __name__ == "__main__":
    print(parser.parse('42').eval())
    print(parser.parse('((2 + 7)*(4-2))').eval())
    print(str(parser.parse('(2+(3*1))')))
    print(parser.parse('(2+(3*1))'))
    print(parser.parse('(2+(3*1))').eval()) """