# Custom 4-bit Processor Assembler

This repository contains an assembler for a custom 4-bit processor built using Logisim. The assembler is capable of converting assembly language instructions into machine code that can be executed by the processor.

## Files

- `Assembler.py`: This is the main assembler script. It contains the `Assembler` class, which is responsible for parsing assembly language instructions and converting them into machine code.

- `file_assemble.py`: This script uses the `Assembler` class to convert an entire file of assembly language instructions into machine code.

## Usage

To use the assembler, you need to have a file containing assembly language instructions. Each instruction should be on a separate line.

Here's an example of how to use the `file_assemble.py` script:

```bash
py file_assemble.py input.txt output.txt
```

In this example, input.txt is the file containing the assembly language instructions, and output.txt is the file where the machine code will be written.

## Assembly Language Syntax

The assembler supports the following opcodes:

- `NOP`: No operation. This instruction does nothing.
- `LD`: Load. This instruction loads a value into a register.
- `MOV`: Move. This instruction moves a value from one register to another.
- `DISP`: Display. This instruction displays the combined value of two registers.
- `XOR`: Bitwise XOR. This instruction performs a bitwise XOR operation on the values of two registers.
- `AND`: Bitwise AND. This instruction performs a bitwise AND operation on the values of two registers.
- `OR`: Bitwise OR. This instruction performs a bitwise OR operation on the values of two registers.
- `ADD`: Add. This instruction adds the values of two registers.
- `SUB`: Subtract. This instruction subtracts the value of one register from another.

Each instruction should be written on a separate line. Operands should be separated by spaces. Register names should be written as R0, R1, etc.

Here's an example of an assembly language program:

```
LD R0 5
LD R1 10
LD R3 3
ADD R2 R0 R1
DISP {R2, R3}
```

This program loads the values 5 and 10 into registers R0 and R1, adds these values and stores the result in R2, and then displays the value of R2 and R3 to the ASCII display.