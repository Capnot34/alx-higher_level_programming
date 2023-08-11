#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div
import sys
def main_program():
    if len(sys.argv) != 4:
       print_usage_and_exit()
    operand1, operator, operand2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    operations = {
        "+": (add, " + "),
	"-": (sub, " - "),
	"*": (mul, " * "),
	"/": (div, " / ")
    }
    operation, symbol = operations.get(operator, (None, None))
    if operation:
	print_unknown_operator_and_exit()
def print_usage_and_exit():
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
if __name__ == "__main__":
    main_program()
