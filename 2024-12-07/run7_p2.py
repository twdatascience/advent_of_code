# Day 7 Part 2
from itertools import product


# define functions
def generate_operator_options(ops, number_ops):
    pos_ops = list(product(ops, repeat=number_ops))
    return pos_ops

def left_to_right(equation_list):
    end = len(equation_list) - 1
    # separate list by element into first 3 then every 2
    first_three = equation_list[:3]
    rest = equation_list[3:]

    if first_three[1] == '||':
        eq_value = int(first_three[0] + first_three[2])
    else:
        eq_value = eval("".join(first_three))
    
    while len(rest) > 0:
        new_eq_part = rest[:2]
        rest = rest[2:]
        
        if new_eq_part[0] == '||':
            eq_value = int(str(eq_value) + new_eq_part[1])
        else:
            eq_value = eval(str(eq_value) + "".join(new_eq_part))
    return eq_value
        

def test_operators(result_in, variables_in, operators_in):
    result_int = int(result_in)
    # find number of operators needed for variables
    num_ops = len(variables_in) - 1
    # generate all possible operator combinations for equation
    op_options = generate_operator_options(operators_in, num_ops)
    # test each combination
    for op_combo in op_options:
        eq_list = [elem for pair in zip(variables, op_combo) for elem in pair] + [variables[-1]]
        # don't follow normal precedence, evaluate left to right
        eq_output = left_to_right(eq_list)
        if eq_output == result_int:
            return True
    return False

# read in input
with open("2024-12-07/input7.txt", "r") as f:
    lines = f.readlines()

# split into result and variables
lines_dict = {}

# could be multiple results that are the same so don't use results as keys
for i in range(len(lines)):
    result, variables = lines[i].strip().split(":")
    variables = variables.strip().split(" ")
    lines_dict[i] = result, variables

operators = ['+', '*', '||']
total_cal = 0
for values in lines_dict.values():
    result, variables = values
    if test_operators(result, variables, operators):
        total_cal += int(result)

print(total_cal)
        