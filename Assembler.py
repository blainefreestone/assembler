import re

VALID_REGISTER_ADDRESSES = {
    'R0': '0000',
    'R1': '0001',
    'R2': '0010',
    'R3': '0011',
    'R4': '0100',
    'R5': '0101',
    'R6': '0110',
    'R7': '0111',
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
        # remove commas, curly brackets, and square brackets from instruction
        instruction = re.sub(r"[,\{\}\[\]\n]", "", instruction)
        # split instruction into opcode and operands
        instruction_parts = instruction.split(' ')
        opcode = instruction_parts[0].upper()
        operands = instruction_parts[1:]

        # check if opcode requires operands
        if not operands and opcode != 'NOP':
            raise ValueError(f"Opcode {opcode} requires operands")
        
        # convert operands to integers or upprcase register names
        for i, operand in enumerate(operands):
            # hexadecimal
            if re.match(r"^0x[a-fA-F0-9]+$", operand):
                operands[i] = int(operand, 16)
            # decimal
            elif re.match(r"^\d+$", operand):
                operands[i] = int(operand)
            # binary
            elif re.match(r"^0b[01]+$", operand):
                operands[i] = int(operand, 2)
            # register
            elif operand.upper() in VALID_REGISTER_ADDRESSES:
                operands[i] = operand.upper()
            else: 
                raise ValueError(f"Invalid operand: {operand}")

        if opcode in self.opcode_map:
            return self.opcode_map[opcode](operands)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

    def handle_no_operation(self, operands):
        # return instruction for no operation
        return '0000000000000000'
    
    def handle_load(self, operands):
        if len(operands) != 2:
            raise ValueError(f"LD opcode requires 2 operands, got {len(operands)}")
        if operands[0] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[0]}")
        if operands[1] not in range(0, 15):
            raise ValueError(f"Invalid data value: {operands[1]}")
        else:
            return f"0001{VALID_REGISTER_ADDRESSES[operands[0]]}0000{operands[1]:04b}"
    
    def handle_move(self, operands):
        if len(operands) != 2:
            raise ValueError(f"LD opcode requires 2 operands, got {len(operands)}")
        if operands[0] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[0]}")
        if operands[1] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[1]}")
        else:
            return f"0010{VALID_REGISTER_ADDRESSES[operands[0]]}{VALID_REGISTER_ADDRESSES[operands[1]]}0000"

    
    def handle_display(self, operands):
        if len(operands) != 2:
            raise ValueError(f"LD opcode requires 2 operands, got {len(operands)}")
        if operands[0] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[0]}")
        if operands[1] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[1]}")
        else:
            return = f"00110000{VALID_REGISTER_ADDRESSES[operands[0]]}{VALID_REGISTER_ADDRESSES[operands[1]]}"
    
    def handle_xor(self, operands):
        if len(operands) not in range(2, 4):
            raise ValueError(f"XOR opcode requires 2 or 3 operands, got {len(operands)}")
        if operands[0] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[0]}")
        if operands[1] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[1]}")
        if len(operands) == 3 and operands[2] not in VALID_REGISTER_ADDRESSES:
            raise ValueError(f"Invalid register: {operands[2]}")
        else:
            destination_register = operands[0]
            operand_register_1 = operands[1]
            if len(operands) == 3:
                operand_register_2 = operands[2]
            else:
                operand_register_2 = operands[1]
            return f"0100{VALID_REGISTER_ADDRESSES[destination_register]}{VALID_REGISTER_ADDRESSES[operand_register_1]}{VALID_REGISTER_ADDRESSES[operand_register_2]}"
    
    def handle_and(self, operands):
        return '0101'
    
    def handle_or(self, operands):
        return '0110'
    
    def handle_add(self, operands):
        return '0111'
    
    def handle_subtract(self, operands):
        return '1000'