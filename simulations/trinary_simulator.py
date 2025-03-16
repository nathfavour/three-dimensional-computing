"""
Trinary Computing Simulator

This module provides a simulation environment for three-dimensional computing
using the states -1, 0, and 1.
"""

class Trit:
    """A single trinary digit with value -1, 0, or 1"""
    
    def __init__(self, value=0):
        """Initialize a trit with a value."""
        if value not in [-1, 0, 1]:
            raise ValueError("Trit value must be -1, 0, or 1")
        self._value = value
        
    @property
    def value(self):
        """Get the current value of the trit."""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Set the value of the trit."""
        if new_value not in [-1, 0, 1]:
            raise ValueError("Trit value must be -1, 0, or 1")
        self._value = new_value
        
    def __repr__(self):
        """Return a string representation of the trit."""
        return f"Trit({self._value})"
    
    def __add__(self, other):
        """Addition operation for trits."""
        if isinstance(other, Trit):
            other = other.value
        
        # Implement trinary addition
        result = self._value + other
        if result > 1:
            return Trit(result - 3)
        elif result < -1:
            return Trit(result + 3)
        return Trit(result)
    
    def __mul__(self, other):
        """Multiplication operation for trits."""
        if isinstance(other, Trit):
            other = other.value
        
        # Simple multiplication
        return Trit(self._value * other)
    
    def __and__(self, other):
        """Trinary AND operation."""
        if isinstance(other, Trit):
            other = other.value
            
        # Trinary AND truth table
        if self._value == -1 or other == -1:
            return Trit(-1)
        elif self._value == 0 or other == 0:
            return Trit(0)
        else:
            return Trit(1)
    
    def __or__(self, other):
        """Trinary OR operation."""
        if isinstance(other, Trit):
            other = other.value
            
        # Trinary OR truth table
        if self._value == 1 or other == 1:
            return Trit(1)
        elif self._value == 0 or other == 0:
            return Trit(0)
        else:
            return Trit(-1)
    
    def __neg__(self):
        """Negation operation for trits."""
        return Trit(-self._value)


class TriWord:
    """A sequence of trits representing a word in trinary computing."""
    
    def __init__(self, values=None, length=4):
        """Initialize a triword with given values or a length."""
        if values:
            self._trits = [Trit(val) for val in values]
        else:
            self._trits = [Trit(0) for _ in range(length)]
    
    def __getitem__(self, index):
        """Get the trit at the specified index."""
        return self._trits[index]
    
    def __setitem__(self, index, value):
        """Set the trit at the specified index."""
        if isinstance(value, Trit):
            self._trits[index] = value
        else:
            self._trits[index] = Trit(value)
    
    def __len__(self):
        """Return the length of the triword."""
        return len(self._trits)
    
    def __repr__(self):
        """Return a string representation of the triword."""
        values = [trit.value for trit in self._trits]
        return f"TriWord({values})"
    
    def to_decimal(self):
        """Convert the triword to decimal value."""
        result = 0
        for i, trit in enumerate(reversed(self._trits)):
            result += trit.value * (3 ** i)
        return result


class TrinaryCPU:
    """Simulates a CPU that works with trinary logic."""
    
    def __init__(self, register_count=8, register_size=8):
        """Initialize the CPU with registers."""
        self.registers = [TriWord([0] * register_size) for _ in range(register_count)]
        self.program_counter = 0
        
    def execute(self, instructions):
        """Execute a sequence of trinary instructions."""
        while self.program_counter < len(instructions):
            instruction = instructions[self.program_counter]
            self.program_counter += 1
            
            # Execute the instruction based on opcode
            if instruction["opcode"] == "ADD":
                src1 = instruction["src1"]
                src2 = instruction["src2"]
                dest = instruction["dest"]
                for i in range(len(self.registers[dest])):
                    self.registers[dest][i] = self.registers[src1][i] + self.registers[src2][i]
            
            elif instruction["opcode"] == "MUL":
                src1 = instruction["src1"]
                src2 = instruction["src2"]
                dest = instruction["dest"]
                for i in range(len(self.registers[dest])):
                    self.registers[dest][i] = self.registers[src1][i] * self.registers[src2][i]
            
            elif instruction["opcode"] == "AND":
                src1 = instruction["src1"]
                src2 = instruction["src2"]
                dest = instruction["dest"]
                for i in range(len(self.registers[dest])):
                    self.registers[dest][i] = self.registers[src1][i] & self.registers[src2][i]
            
            elif instruction["opcode"] == "OR":
                src1 = instruction["src1"]
                src2 = instruction["src2"]
                dest = instruction["dest"]
                for i in range(len(self.registers[dest])):
                    self.registers[dest][i] = self.registers[src1][i] | self.registers[src2][i]
            
            elif instruction["opcode"] == "LOAD":
                value = instruction["value"]
                dest = instruction["dest"]
                self.registers[dest] = TriWord(value)
                
            elif instruction["opcode"] == "HALT":
                break
    
    def get_register(self, reg_num):
        """Get the value of a register."""
        return self.registers[reg_num]


# Example usage of the simulator
if __name__ == "__main__":
    # Create a sample program
    program = [
        {"opcode": "LOAD", "value": [1, 0, -1, 1], "dest": 0},
        {"opcode": "LOAD", "value": [0, 1, -1, 0], "dest": 1},
        {"opcode": "ADD", "src1": 0, "src2": 1, "dest": 2},
        {"opcode": "MUL", "src1": 0, "src2": 1, "dest": 3},
        {"opcode": "HALT"}
    ]
    
    # Create and run the CPU
    cpu = TrinaryCPU()
    cpu.execute(program)
    
    # Print results
    print("Register 0:", cpu.get_register(0))
    print("Register 1:", cpu.get_register(1))
    print("Register 2 (Addition Result):", cpu.get_register(2))
    print("Register 3 (Multiplication Result):", cpu.get_register(3))
    
    # Demonstrate conversions
    print("\nDecimal value of Register 0:", cpu.get_register(0).to_decimal())
    print("Decimal value of Register 1:", cpu.get_register(1).to_decimal())
    print("Decimal value of Register 2:", cpu.get_register(2).to_decimal())
