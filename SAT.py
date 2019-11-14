import re
import itertools
import numpy as np

#=====================================================================

# # function to evaluate each clause
# def eval_cl(clau):
#     clau = sorted(set(filter(None,re.split(r'[|)(]+',clau))))
#     print(clau,'\n')

#=====================================================================

# function to evaluate expression
def eval_exp(vr_list,expression):
    total_var = len(vr_list)
    expression = expression.replace('~',' not ')
    
    print("TURTH TABLE")
    print("===============================================\n")
    for var in vr_list:
        print(var,end = "  |  ")
    print("ans")        
    print("===============================================")
    for i in itertools.product([0,1], repeat=total_var):
        exp_cp = expression # copy of expression
        n = -1
        for var in vr_list:
            n+=1
            exp_cp = exp_cp.replace(var,str(i[n]))
            print(str(i[n]),end="  |  ")
        exec("print(\"\","+exp_cp+")")   
        a = eval(exp_cp)
            
# input expression
in_exp = "( a |b|( ~c))&((~a )|c)&((~b)|c )&((~d)|(~ e)|(~f ))&(( d )|(e)|( ~ f) )&((  d)|(~  e) |( f))&((~d)|(e)|(f))&((~e)|(~f)|(~g))&((e)|(f)|(~g))&((e)|(~f)|(g))&((~e)|(f)|(g))&g"

# in_exp = "((~a )|c)"
in_exp = re.sub(r'\s+', '', in_exp) # removing white spaces

#=====================================================================

# # seperating into list of clauses
# cl_list = sorted(in_exp.split('&'), key=len)

#=====================================================================

# list of variables
vr_list = sorted(set(filter(None,re.split(r'[|&)(~]+',in_exp))))

# print truth table
eval_exp(vr_list, in_exp)

#=====================================================================
# for i in cl_list:
#     print(i)
#     eval_cl(i)
#=====================================================================
