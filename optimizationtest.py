# CITATION: 
# https://towardsdatascience.com/solving-your-first-linear-program-in-python-9e3020a9ad32

from scipy.optimize import linprog
import numpy as np

# creating a strawberry banana smoothie

# Equations to solve
# variables: s = strawberries, b = bananas, m = milk, y = yogurt
# s + b + m + y = 75 (all ingredients summed should be 75 g)
# y - 2m = 0 (yogurt is 2x milk)
# s + b <= 50 (strawberry + banana is no more than 50 g)
# s + y <= 30 (strawberry + yogurt is no more than 30 g)
# s - b + m - y <= 0 (sum of strawberry and milk is no more than sum of banana and yogurt)

# X matrix
var_list = ['Strawberries', 'Bananas', 'Milk', 'Yogurt']

# Inequality equations, LHS
A_ineq = [[1., 1., 0., 0.], [1., 0., 0., 1.], [1., -1., 1., -1.]]

# Inequality equations, RHS
B_ineq = [50., 30., 0.]

# Equality equations, LHS
A_eq = [[1., 1., 1., 1.], [0., 0., -2., 1.]]

# Equality equations, RHS
B_eq = [75., 0.]

# Cost function
c = [0., 0., 1., 1.]  # construct a cost function

print('WITHOUT BOUNDS')
# pass these matrices to linprog, use the method 'interior-point'. '_ub' implies 
# the upper-bound or inequality matrices and '_eq' imply the equality matrices
res_no_bounds = linprog(c, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, method='interior-point')
print(res_no_bounds)