from ply import lex

tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'IDENTIFIER', 'ASSIGN')

t_ASSIGN = r'<-'
t_IDENTIFIER = r'[a-z][a-zA-Z0-9]*'
t_NUMBER = r'[0-9]+(\.[0-9]+)?'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)' 
t_ignore = ' '
t_error = lambda t: print(f"Illegal character '{t.value[0]}'") or t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__" :
    lexer.input('42')
    for tok in lexer :
        print(tok)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    lexer.input('(2 + 3)')
    for tok in lexer:
        print(tok)