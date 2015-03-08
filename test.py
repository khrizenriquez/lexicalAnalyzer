import collections
import re
from rules.analyzerRules import *
from classes.Entry import *

Token = collections.namedtuple('Token', ['typ', 'value', 'line'])

#   Source http://stackoverflow.com/questions/133886/simple-regex-based-lexer-in-python
def tokenize(s):
    words = reserveWords
    token_specification = [
        ('RESEVE_WORDS', r'new|var|if|else|for|in|while|do|switch|case|default|break|continue|function|this|continue|true|false|try|catch|return|union'),
        ('NUMBER',  r'\d+(\.\d*)?'), # Integer or decimal number
        ('ASSIGN',  r':='),           # Assignment operator
        ('END',     r';'),           # Statement terminator
        ('ID',      r'[A-Za-z]+'),   # Identifiers
        ('OP',      r'[+*\/\-]'),    # Arithmetic operators
        ('NEWLINE', r'\n'),          # Line endings
        ('SKIP',    r'[ \t]'),       # Skip over spaces and tabs
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = 1
    pos = line_start = 0
    mo = get_token(s)
    while mo is not None:
        typ = mo.lastgroup
        if typ == 'NEWLINE':
            line_start = pos
            line += 1
        elif typ != 'SKIP':
            val = mo.group(typ)
            if typ == 'ID' and val in words:
                typ = val
            yield Token(typ, val, line)
        pos = mo.end()
        mo = get_token(s, pos)
    if pos != len(s):
        raise RuntimeError('Unexpected character %r on line %d' %(s[pos], line))

statements = '''
    if quantity then
        total := total + price * quantity;
        tax := price * 0.05;
    endif;
'''

for token in tokenize(statements):
    print(token)