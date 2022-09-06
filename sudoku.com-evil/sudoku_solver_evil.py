#!/usr/bin/env python
# coding: utf-8

# import pre-filled numbers
from evil1.starting_numbers  import pre_fill

import time as time

# for using CPLEX within Python
from docplex.mp.model import Model

# for timing the code
start_time = time.time()

# $N = {1, 2, ..., 9}$: The set of numbers
N = list(range(1,10))

# Create a CPLEX model object
sudoku = Model(name='sudoku-mip')

# Decision Variables
x = sudoku.binary_var_dict(keys = [(i, j, k) for i in N for j in N for k in N], name="x")

# There is no objective function. We just need to find a solution that satisfies all of the constraints. Thus, we can just set the objective function to 
sudoku.minimize(0)

# ## Constraints

# Each number appears in each row exactly once
sudoku.add_constraints(sudoku.sum(x[(i,j,k)] for j in N) == 1 for i in N for k in N)

# Each number appears in each column exactly once
sudoku.add_constraints(sudoku.sum(x[(i,j,k)] for i in N) == 1 for j in N for k in N)

# Each cell (row,column) has exactly one number
sudoku.add_constraints(sudoku.sum(x[(i,j,k)] for k in N) == 1 for i in N for j in N)

# Each number appears exactly once in each of the designated 3x3 boxes
a_b_set = [0,3,6]
sudoku.add_constraints(sudoku.sum(x[(i+a,j+b,k)] for i in N[:3] for j in N[:3] ) == 1 for a in a_b_set for b in a_b_set for k in N)

sudoku.add_constraints(x[cell] == 1 for cell in pre_fill)


# Solve the problem
sudoku.solve()

# Write Solution in Sudoku Format
with open('sudoku.com-evil/evil1/sudoku_solution.txt', 'w+') as sol_file:

    for i in N:
        if i in [1,4,7]:
            sol_file.write("+-------+-------+-------+\n")

        for j in N:
            for k in N:
                if sudoku.solution.get_value(x[(i,j,k)]):
                    if j in [1,4,7]:
                        sol_file.write("| ")

                    sol_file.write(f"{k} ")

                    if j == 9:
                        sol_file.write("|\n")

    sol_file.write("+-------+-------+-------+") 

print(f"Runtime: {round(time.time()-start_time,2)} seconds")
print("Finished")