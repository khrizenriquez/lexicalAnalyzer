#	Operators
reserveWords = {
    'new', 
    'var', 
    'if', 
    'else', 
    'for', 
    'in', 
    'while', 
    'do', 
    'switch', 
    'case', 
    'default', 
    'break', 
    'continue', 
    'function', 
    'this', 
    'continue', 
    'true', 
    'false', 
    'try', 
    'catch', 
    'return'
}

# Identifiers
idValues			= r'[a-zA-Z_][a-zA-Z0-9_]*'
# Integer or decimal number
numbers 			= r'\d+(\.\d*)?'
# Arithmetic operators
aritmeticOperatos 	= r'[+*\/\-]'
# Line endings
newLine 			= r'\n'
# Skip over spaces and tabs
skipValues 			= r'[ \t]'
# Skip over spaces and tabs
logicOperators 		= r'and|or|not'
terminals 			= r'{|[|(|)|]|}|;|:|.'
relationalOperators = r'<=|>=|<|>|===|==|!='
