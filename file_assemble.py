import sys
from Assembler import Assembler

if len(sys.argv) not in range(2, 4):
    print("Usage: py file_assemble.py <input_file> <output_file>")
    sys.exit(1)
elif len(sys.argv) == 2:
    input_file = sys.argv[1]
    output_file = "output.txt"
elif len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

assembler = Assembler()

with open(input_file, 'r') as f:
    with open(output_file, 'w') as output:
        for index, line in enumerate(f):
            try:
                output.write(assembler.assemble(line) + '\n')
            except ValueError as e:
                print(f"Error on line {index + 1}:\n {e}")
                sys.exit(1)