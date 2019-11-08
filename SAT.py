import re

# define symbols
sym_AND = '&'

# input expression
in_exp = "( a |b|( ~c))&((~a )|c)&((~b)|c )&((~d)|(~ e)|(~f ))&(( d )|(e)|( ~ f) )&((  d)|(~  e) |( f))&((~d)|(e)|(f))&((~e)|(~f)|(~g))&((e)|(f)|(~g))&((e)|(~f)|(g))&((~e)|(f)|(g))&g&(~g)"
in_exp = re.sub(r'\s+', '', in_exp) # removing white spaces

# seperating into list of clauses
cl_list = sorted(in_exp.split(sym_AND), key=len)


# list of variables
vr_list = sorted(set(filter(None,re.split(r'[|&)(~]+',in_exp))))
