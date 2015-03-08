#
from rules.analyzerRules import * 
import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line'])

class Entry:
	def __init__(self):
		self.code = """var Khriz = 22;
		var Enriquez = 20;
		var i;
		"Khriz enriquez es un loquillo"
"""

	#Return the user script
	def userScript (self):
		#return self.other
		return self.code

	#   Source http://stackoverflow.com/questions/133886/simple-regex-based-lexer-in-python
	def tokenize (self, value, rWords):
	    words = rWords
	    token_specification = [
	    	#Values come from analyzerRules.py
	        ('Numero',  			numbers), 
	        ('Asignacion',  		r'='),           	# Assignment operator
	        #('END',     r';'),           	# Statement terminator
	        ('ID',      			idValues), 
	        ('OperadorAritmetico',  aritmeticOperatos), 
	        ('NuevaLinea', 			newLine), 
	        ('SKIP',    			skipValues), 
	        ('Terminal',    		terminals), 
	        ('OperadorRelacional',  relationalOperators), 
	        ('OperadorLogico', 		logicOperators)
	    ]

	    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
	    get_token = re.compile(tok_regex).match
	    line = 1
	    pos = line_start = 0
	    mo = get_token(value)

	    while mo is not None:
	        typ = mo.lastgroup
	        if typ == 'NuevaLinea':
	            line_start = pos
	            line += 1
	        elif typ != 'SKIP':
	            val = mo.group(typ)
	            if typ == 'ID' and val in words:
	                typ = val
	            yield Token(typ, val, line)
	        pos = mo.end()
	        mo = get_token(value, pos)
	    if pos != len(value):
	        raise RuntimeError('Unexpected character %r on line %d' %(value[pos], line))