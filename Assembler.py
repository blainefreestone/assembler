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
        instruction_parts = instruction.split(' ')
        opcode = instruction_parts[0]
        operands = instruction_parts[1:]
        
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