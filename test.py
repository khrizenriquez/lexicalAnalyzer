import collections
import re
from rules.analyzerRules import *
from classes.Entry import *

Token = collections.namedtuple('Token', ['typ', 'value', 'line'])


statements = '''
    if quantity then
        total := total + price * quantity;
        tax := price * 0.05;
    endif;
'''

for token in tokenize(statements):
    print(token)