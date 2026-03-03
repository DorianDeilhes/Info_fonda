# Calculator Project

A simple calculator built with PLY (Python Lex-Yacc) that supports arithmetic expressions with variables and assignments.

## Features

- **Arithmetic operations**: `+`, `-`, `*`, `/`
- **Floating-point numbers**: `3.14`, `2.5`, etc.
- **Variables and assignments**: `x <- 5`, `y <- x + 3`
- **Parentheses**: `(2 + 3) * 4`
- **Unary minus**: `-5`, `-(x + 2)`
- **Operator precedence**: Follows standard mathematical rules

## Project Structure

```
calculator/
├── arithmetic_expressions.py  # AST (Abstract Syntax Tree) classes
├── arithmetic_lexer.py        # Lexer (tokenization)
├── arithmetic_parser.py       # Parser (grammar rules)
└── calculatrice.py           # Interactive calculator interface
```

## Usage

Run the interactive calculator:

```bash
python calculator/calculatrice.py
```

### Examples

```
calc > 2 + 3
5.0
calc > x <- 10
10.0
calc > x * 2.5
25.0
calc > (x + 5) / 3
5.0
```

Type `exit` or `quit` to exit the calculator.

## Requirements

- Python 3.x
- PLY (Python Lex-Yacc) - included in the `ply/` directory
