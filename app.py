input_file = open('data/a_example.in', "r")

import solver
solver.input = input_file.readline
solver.run()
