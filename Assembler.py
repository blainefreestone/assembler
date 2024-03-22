import re

VALID_REGISTER_ADDRESSES = {
    'R0': '0000',
    'R1': '0001',
    'R2': '0010',
    'R3': '0011',
    'R4': '0100',
    'R5': '0101',
    'R6': '0110',
    'R7': '0111'
}

class Assembler:
    def __init__(self):
        # define map with callback functions for each opcode
        self.opcode_map = {
            'NOP': self.handle_no_operation,
            'LD': self.handle_load,
            'MOV': self.handle_move,
            'DISP': self.handle_display,
            'XOR': self.handle_xor,
            'AND': self.handle_and,
            'OR': self.handle_or,
            'ADD': self.handle_add,
            'SUB': self.handle_subtract
        }

    def assemble(self, instruction):
        # split instruction into opcode and operands
        instruction_parts = instruction.split(' ')
        opcode = instruction_parts[0]
        operands = instruction_parts[1:]

        # check if opcode requires operands
        if not operands and opcode != 'NOP':
            raise ValueError(f"Opcode {opcode} requires operands")
        
        # convert operands to integers or register names
        for i, operand in enumerate(operands):
            # hexadecimal
            if re.match(r"0x[a-fA-F0-9]+", operand):
                operands[i] = int(operand, 16)
            # decimal
            elif re.match(r"\d+", operand):
                operands[i] = int(operand)
            # binary
            elif re.match(r"0b[01]+", operand):
                operands[i] = int(operand, 2)
            # register
            elif operand in VALID_REGISTER_ADDRESSES:
                pass
            else: 
                raise ValueError(f"Invalid operand: {operand}")

        if opcode.upper() in self.opcode_map:
            return self.opcode_map[opcode](operands)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    def handle_no_operation(self, operands):
        # return instruction for no operation
        return '0000000000000000'
    
    def handle_load(self, operands):
        return '0001'
    
    def handle_move(self, operands):
        return '0010'
    
    def handle_display(self, operands):
        return '0011'
    
    def handle_xor(self, operands):
        return '0100'
    
    def handle_and(self, operands):
        return '0101'
    
    def handle_or(self, operands):
        return '0110'
    
    def handle_add(self, operands):
        return '0111'
    
    def handle_subtract(self, operands):
        return '1000'