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

logicOperators 		= 'and|or|not|var'
terminals 			= '{|[|(|)|]|}'
relationalOperators = '<=|>=|<|>|===|==|!=|='
numbers 			= '[0-9]*'
addition 			= ''
ID 					= r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS    			= r'\+'
t_MINUS   			= r'-'
t_TIMES   			= r'\*'
t_DIVIDE  			= r'/'
t_EQUALS  			= r'='
# Ignored characters
t_ignore = " \t"
