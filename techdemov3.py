import module_manager
module_manager.review()
from scipy.optimize import linprog
import numpy as np
from cvxopt import matrix
from cvxopt import glpk


# The perfect cake recipe that I partially remember

# Equations to solve
# f + e + b + s = 700
# b -0.5s = 0
# f + e <= 450
# e + b <= 300
# -f + e + b -s <= 0

# X matrix
var_list = ['Flour', 'Eggs', 'Butter', 'Sugar']

# Inequality equations, LHS
A_ineq = [[1., 1., 0., 0.], [0., 1., 1., 0.], [-1., 1., -1., 1.]]

# Inequality equations, RHS
B_ineq = [450., 300.,0.]

# Equality equations, LHS
A_eq = [[1., 1., 1., 1.], [0., 0., 1., -0.5]]

# Equality equations, RHS
B_eq = [700., 0]

# Cost function
c = [0., 0., 1., 1.]  # construct a cost function

print('WITHOUT BOUNDS')
# pass these matrices to linprog, use the method 'interior-point'. '_ub' implies the upper-bound or
# inequality matrices and '_eq' imply the equality matrices
res_no_bounds = linprog(c, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, method='interior-point')
print(res_no_bounds)