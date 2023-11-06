# # Example
# This script contains an example of how to use the code in the repo
# First let us import the libraries we need

import fermat_solver

# Next let ut try to check the solution of the equation
#
# $$ 3^2 + 4^2 == 5^2 $$
#

fermat_solver.check_solution(x=3, y=4, z=5, n=2)

# It works! But how about
#
# $$ 3^3 + 4^3 == 5^3 $$
#

fermat_solver.check_solution(x=3, y=4, z=5, n=3)

# Nope, this is not
