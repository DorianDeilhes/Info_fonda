#Calculatrice interactive en ligne de commande
from arithmetic_parser import parser

if __name__ == "__main__":
    env = {}  # Persistent environment to store variables
    print("Calculator with variables and assignments")
    print("Use: x <- 5 to assign, x+3 to use variables")
    print("Type 'exit' or 'quit' to quit\n")
    
    while True:
        try:
            s = input('calc > ')
            if s.lower() in ('exit', 'quit'):
                print("Goodbye!")
                break
            result = parser.parse(s)
            if result is not None:
                print(result.eval(env))  # Pass persistent environment
        except Exception as e:
            print(f"Error: {e}")