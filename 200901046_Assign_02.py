import re
#import re module from python

import ast
#import AST module from python for parsing

# Define the tokens
PLUS = r'\+'
MINUS = r'-'
TIMES = r'\*'
DIVIDE = r'/'
LPAREN = r'\('
RPAREN = r'\)'
ID = r'[a-zA-Z][a-zA-Z0-9]*'
INTEGER = r'\d+'

def tokenize(expression):
    output = []
  # Use the regular expression to find all tokens in the input string
    for token in expression:
        
        if token == ' ':
            pass 
        elif re.match(ID,token):
            output.append(("Identifier",token))
        elif re.match(INTEGER,token):
            output.append(("Constant",token))
        elif re.match(LPAREN,token) or re.match(RPAREN,token):
            output.append(('Punctuator',token))
        elif re.match(PLUS,token) or re.match(MINUS,token) or re.match(TIMES,token) or re.match(DIVIDE,token):
            output.append(('Operator',token)) 
        else:
            output.append(('Special Character',token))
        
    for i in output: 
        print(i)

#func for parsing expression
def parse_expression(expression):
  return ast.parse(expression)

def print_ast(tree):
      print(ast.dump(tree,indent = 2))
      
 #main function     
if __name__ == '__main__':
        
    print('Parse Tree')      
    expression = "a + b * c"
    tree = parse_expression(expression)
    print_ast(tree)

    print('Lexical Analyzer')                        
    # Test the tokenize function
    expression = input("Enter the expression e.g(a+b): ")
    tokenize(expression)