# sudoku-mip-solver
This repo shows how to solve Sudoku puzzles using Mixed Integer Linear Programming (MILP)

# Requirements
In order to run the code in this repo, you need the following:
* Python
* An IDE that can handle Jupyter Notebooks
* CPLEX

CPLEX is a state of the art mathematical programming solver by IBM. You can obtain a free edition from IBM [here](https://www.ibm.com/products/ilog-cplex-optimization-studio?utm_content=SRCWW&p1=Search&p4=43700068101114280&p5=p&gclid=CjwKCAjwvNaYBhA3EiwACgndglgnVltJEYfTYCikjZeehtyYqGVqypBytS5AJA1fS0xdMHaOb0gXtRoC7aUQAvD_BwE&gclsrc=aw.ds). 

# Starting out
I recommend looking at the [sudoku.ipynb](https://github.com/sj7stark/sudoku-mip-solver/blob/main/sudoku.ipynb) first. It contains:
* A brief introduction regarding Sudoku
* The components of the MILP written out, along with the corresponding code

# Evil Sudoku

[sudoku.com](https://sudoku.com/) is a website where you can solve Sudokus online for free. They have problems that vary in difficulty from Easy to Evil. The Evil problems may be difficult for a human, but they are no match for this model.

