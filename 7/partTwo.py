import itertools

with open('input.txt', 'r') as f:
    input_data = [int(x) for x in f.read().strip('\n').split(',')]

class Amplifier:
    def __init__(self, program, phase):
        self.program = program[:] # Copy mutable list to avoid overriding it
        self.phase = phase
        self.initialised = False
        self.i = 0

    def parse_parameter_mode_and_opcode(self, pair):
        if len(str(pair)) == 1:
            opcode = pair
            parameter_modes = 0
        else:
            opcode = pair % 100
            parameter_modes = int((pair - opcode) / 100)
        return {'opcode': opcode, 'parameter_modes': parameter_modes}

    def run(self, input, log = False):
        length = len(self.program)
        input_count = 1
        while self.i < length:
            instruction_length = 2
            if log:
                instruction = str(self.program[self.i]) + ', ' + str(self.program[self.i + 1])
            parsed = self.parse_parameter_mode_and_opcode(self.program[self.i])
            opcode = parsed['opcode']
            parameter_modes = str(parsed['parameter_modes'])
            if opcode in [1, 2, 5, 6, 7, 8]:
                parameter_mode_1 = 0 if len(parameter_modes) < 1 else int(parameter_modes[len(parameter_modes) - 1])
                parameter_1 = int(self.program[self.i + 1]) if parameter_mode_1 == 1 else self.program[self.program[self.i + 1]]
                parameter_mode_2 = 0 if len(parameter_modes) < 2 else int(parameter_modes[len(parameter_modes) - 2])
                parameter_2 = int(self.program[self.i + 2]) if parameter_mode_2 == 1 else self.program[self.program[self.i + 2]]
                instruction_length = 3
                if log:
                    instruction += ', ' + str(self.program[self.i + 2])
                if opcode in [1, 2, 7, 8]:
                    parameter_3 = self.program[self.i + 3]
                    instruction_length = 4
                    if log:
                        instruction += ', ' + str(self.program[self.i + 3])
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
                val = self.phase if not self.initialised else input
                if not self.initialised:
                    self.initialised = True
                position = self.program[self.i + 1]
                if log:
                    print('Putting val ' + str(val) + ' at position ' + str(position))
                self.program[position] = val
                if log:
                    print(self.program)
                input_count += 1
            elif opcode == 4:
                # Output integer
                parameter = self.program[self.i + 1]
                output = parameter if int(parameter_modes[len(parameter_modes) - 1]) == 1 else self.program[parameter]
                if log:
                    print('Outputting: ' + str(output))
                self.i += 2
                return output
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
            elif opcode == 99:
                # End program
                if log:
                    print('Ending program!')
                return 'HALT'
            self.i += instruction_length
        return 'HALT'

def calculate_output_signal(phases):
    input = 0
    amps = []
    for phase in phases:
        amps.append(Amplifier(input_data, phase))

    while input != 'HALT':
        amp_count = 1
        for amp in amps:
            input = amp.run(input)
            if amp_count == 5:
                amp_5_output = input
            if input == 'HALT':
                break
            amp_count += 1
    return amp_5_output

def find_highest_output_signal():
    phases_list = list(itertools.permutations([5, 6, 7, 8, 9]))
    output_signals = []
    for phases in phases_list:
        output_signals.append(calculate_output_signal(phases))
    return max(output_signals)

print(find_highest_output_signal())