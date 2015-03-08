# -*- coding: utf-8 -*-
"""*
*	Khriz Enríquez @khrizenriquez
*	Lexical analyzer
*"""

#	Import clases and functions
from classes.Entry import *
from rules.analyzerRules import *
import collections
import re

i 				= Entry()
data 			= i.userScript().splitlines()
breakLines 		= (len(data) - 1)


#Drawing the values table, that contain:
#Palabra reservada = Pr
#Id = Id
#Constante = Cons
#Operadores = Op
#Operadores relacionales = Op rel
#Terminal = terminal

#	Removing duplicate values, source: http://www.thecapybara.com/2010/09/nota-python-eliminar-elementos.html
def data (titleObj, typeObj, dataObj):
	json = {
		titleObj: {
			typeObj: dataObj
		}
	}
	print json

lineNumber = 0
formatedWords = []
for token in i.tokenize(i.userScript(), reserveWords):
	try:
		#	Compare my variable with token.line value, if is equal add in my list the values
		if lineNumber == token.line:
			#formatedWords.append()
			print token.typ + ': ' + token.value
			formatedWords.append(token.value)
			formatedWords.append(token.typ)
			#data(token.typ)
			#print list(set(formatedWords))
		else:
			lineNumber = int(token.line)
			formatedWords = []
			print 'Línea_______________________________________________ ' + str(lineNumber)
	except Exception, e:
		''

#data('k', 'K', 1)
"""for index, x in enumerate(data, start = 1):

	print '__________________________________________________________________________ Línea ' + str(index)

	#		split values, omit blank spaces
	splitValue = x.split(' ')

	for indexInception, inception in enumerate(splitValue, start = 1):
		#	Reserved words loop
		a = re.match(reservedWords, inception)
		#	Logic operators loop
		b = re.match(logicOperators, inception)
		#	Terminals loop
		c = re.match(terminals, inception)
		#	Relational Operators loop
		d = re.match(relationalOperators, inception)
		#	Numbers
		e = re.match(numbers, inception)

		if (a != None):
			try:
				rWords.append(a.group(0))
			except Exception, e:
				''
		elif (b != None):
			try:
				opLogics.append(b.group(0))
			except Exception, e:
				''
		elif (c != None):
			try:
				terminal.append(c.group(0))
			except Exception, e:
				''
		elif (d != None):
			try:
				relOperator.append(d.group(0))
			except Exception, e:
				''
		elif (e != None):
			try:
				numberValues.append(e.group(0))
			except Exception, e:
				''
	print 'Palabras reservadas: ' + str(list(set(rWords)))
	print 'Operadores lógicos: ' + str(list(set(opLogics)))
	print 'Terminales: ' + str(list(set(terminal)))
	print 'Operadores relacionales: ' + str(list(set(relOperator)))
	print 'Operadores relacionales: ' + str(list(set(numberValues)))

	#	opLogics.append(words)

	#	operators loop
	#c = re.match(aritmeticOperators, x)
	#print re.findall(operators, x)
	#try:
	#	op.append(c.group(0))
	#except Exception, e:
	#	''
	#for words in re.findall(operators, x):
		#print words
		#op.append(words)
print "----------------------------------------------"
rWords = list(set(rWords))
print rWords, 'reserved words'

opLogics = list(set(opLogics))
print opLogics, 'logic operatores'

terminal = list(set(terminal))
print terminal, 'Terminales'

relOperator = list(set(relOperator))
print relOperator, 'relOperator'
"""
#op = list(set(op))
#print op, 'operator'
