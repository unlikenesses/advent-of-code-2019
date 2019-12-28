with open('input.txt', 'r') as f:
    input_data = [int(x) for x in f.read().strip('\n').split(',')]

extra_memory = [0] * 256

input_data = input_data + extra_memory

class Computer:
    def __init__(self, program):
        self.program = program[:] # Copy mutable list to avoid overriding it
        self.i = 0
        self.relative_base = 0

    def parse_parameter_mode_and_opcode(self, pair):
        if len(str(pair)) == 1:
            opcode = pair
            parameter_modes = 0
        else:
            opcode = pair % 100
            parameter_modes = int((pair - opcode) / 100)
        return {'opcode': opcode, 'parameter_modes': parameter_modes}

    def get_parameter(self, parameter_modes, ordinal):
        parameter_mode = 0 if len(parameter_modes) < ordinal else int(parameter_modes[len(parameter_modes) - ordinal])
        if parameter_mode == 1:
            # Immediate mode
            parameter = int(self.program[self.i + ordinal])
        elif parameter_mode == 2:
            # Relative mode
            parameter = self.program[self.program[self.i + ordinal] + self.relative_base]
        else:
            # Position mode
            parameter = self.program[self.program[self.i + ordinal]]
        return parameter

    def run(self, log = False):
        length = len(self.program)
        while self.i < length:
            instruction_length = 2
            if log:
                instruction = str(self.program[self.i]) + ', ' + str(self.program[self.i + 1])
            parsed = self.parse_parameter_mode_and_opcode(self.program[self.i])
            opcode = parsed['opcode']
            parameter_modes = str(parsed['parameter_modes'])
            if opcode in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                # Opcode has at least 1 parameter:
                parameter_1 = self.get_parameter(parameter_modes, 1)
                instruction_length = 2
                if opcode in [1, 2, 5, 6, 7, 8]:
                    # Opcode has at least 2 parameters:
                    parameter_2 = self.get_parameter(parameter_modes, 2)
                    instruction_length = 3
                    if log:
                        instruction += ', ' + str(parameter_2)
                if opcode in [1, 2, 7, 8]:
                    # Opcode has 3 parameters:
                    parameter_mode = 0 if len(parameter_modes) < 3 else int(parameter_modes[len(parameter_modes) - 3])
                    if parameter_mode == 1:
                        # Immediate mode
                        pass # Makes no sense in this context
                    elif parameter_mode == 2:
                        # Relative mode
                        parameter_3 = self.program[self.i + 3] + self.relative_base
                    else:
                        # Position mode
                        parameter_3 = self.program[self.i + 3]
                    instruction_length = 4
                    if log:
                        instruction += ', ' + str(parameter_3)
            if log:
                print('Opcode: ' + str(opcode) + ' at position ' + str(self.i) + '; parameter modes: ' + parameter_modes + ' (instr: ' + instruction + ')')
            if opcode == 1:
                # Add parameters
                if log:
                    print('Adding: ', parameter_1, parameter_2)
                self.program[parameter_3] = int(parameter_1) + int(parameter_2)
            elif opcode == 2:
                # Multiply parameters
                if log:
                    print('Multiplying: ', parameter_1, parameter_2)
                self.program[parameter_3] = int(parameter_1) * int(parameter_2)
            elif opcode == 3:
                # Ask for input integer and store it
                val = input('Speak to me: ')
                parameter_mode = 0 if len(parameter_modes) < 1 else int(parameter_modes[len(parameter_modes) - 1])
                if parameter_mode == 1:
                    # Immediate mode
                    pass # Makes no sense in this context
                elif parameter_mode == 2:
                    # Relative mode
                    position = self.program[self.i + 1] + self.relative_base
                else:
                    # Position mode
                    position = self.program[self.i + 1]
                if log:
                    print('Putting val ' + str(val) + ' at position ' + str(position))
                self.program[position] = val
            elif opcode == 4:
                # Output integer
                print(parameter_1)
            elif opcode == 5:
                # Jump-if-true
                if parameter_1 != 0:
                    self.i = parameter_2
                    continue # Avoid the pointer increment at the end of this loop
            elif opcode == 6:
                # Jump-if-false
                if parameter_1 == 0:
                    self.i = parameter_2
                    continue # Avoid the pointer increment at the end of this loop
            elif opcode == 7:
                # Less-than
                self.program[parameter_3] = 1 if int(parameter_1) < int(parameter_2) else 0
            elif opcode == 8:
                # Equals
                self.program[parameter_3] = 1 if int(parameter_1) == int(parameter_2) else 0
            elif opcode == 9:
                # Modify relative base
                self.relative_base += parameter_1
                if log:
                    print('New relative base = ' + str(self.relative_base))
            elif opcode == 99:
                # End program
                if log:
                    print('Ending program!')
                return 'HALT'
            self.i += instruction_length
        return 'END'

computer = Computer(input_data)
output = computer.run()
print(output)
