import numpy as np
import Factorization as fct
import MultiPartition as mp
import math


def optimal_stucture(mult_factor, mode='short'):
    """Calculate optimal structure"""
    super_v = []
    for f in mult_factor:
        for f_in in f:
            super_v.append(f_in)

    s_v = []
    sum_fact_v = 0
    for f in super_v:
        h_fact = 1 / len(f)
        lol = [(i, f.count(i)) for i in set(f)]
        temp = 1
        for l in lol:
            temp *= math.factorial(l[1])
        abs_fact_i_v = math.factorial(len(f)) / temp
        sum_fact_v += abs_fact_i_v
        s_v.append([[f], h_fact, abs_fact_i_v])

    s_v_2 = []
    sum_h_v = 0
    for f in s_v:
        fact_v_and_v_i = f[2] / sum_fact_v
        sum_h_v += f[1] * fact_v_and_v_i
        s_v_2.append([f[0], f[2], sum_fact_v, fact_v_and_v_i, f[1]])

    s_v_3 = []
    for f in s_v_2:
        temp = f
        temp.append(sum_h_v)
        temp.append(math.fabs(f[-1] - f[4]))
        s_v_3.append(temp)
    s_v_3 = sorted(s_v_3, key=lambda x: x[-1])
    if mode == 'short':
        final_goal = []
        old_number = []
        flag = True
        for f in s_v_3:
            if len(f[0][0]) not in old_number:
                old_number.append(len(f[0][0]))
                final_goal.append([len(f[0][0]), f[-1]])
            else:
                pass
        return final_goal
    elif mode == 'full':
        return s_v_3


x = np.random.randint(2, size=[8, 8])
# print(x)
# example = np.array([[11, 21], [12, 21],
#                     [13, 22], [14, 22]])

factor_list = fct.get_final_factor_list(x)
result = optimal_stucture(factor_list)

for r in result:
    print(r)
