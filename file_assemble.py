import sys
from Assembler import Assembler

if len(sys.argv) != 2:
    print("Usage: py file_assemble.py <input_file>")
    sys.exit(1)
else:
    input_file = sys.argv[1]

assembler = Assembler()

with open(input_file, 'r') as f:
    with open("A:\\School\\Winter 2024\\ECEN240\\output.txt", 'w') as output:
        for line in f:
            try:
                output.write(assembler.assemble(line) + '\n')
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(1)