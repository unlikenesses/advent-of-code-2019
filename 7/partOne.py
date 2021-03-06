import itertools

with open('input.txt', 'r') as f:
    input_data = [int(x) for x in f.read().strip('\n').split(',')]

def parse_parameter_mode_and_opcode(pair):
    if len(str(pair)) == 1:
        opcode = pair
        parameter_modes = 0
    else:
        opcode = pair % 100
        parameter_modes = int((pair - opcode) / 100)
    return {'opcode': opcode, 'parameter_modes': parameter_modes}

def run(program, input_1, input_2, log = False):
    program = program[:] # Copy mutable list to avoid overriding it
    length = len(program)
    i = 0
    input_count = 1
    while i < length:
        instruction_length = 2
        if log:
            instruction = str(program[i]) + ', ' + str(program[i + 1])
        parsed = parse_parameter_mode_and_opcode(program[i])
        opcode = parsed['opcode']
        parameter_modes = str(parsed['parameter_modes'])
        if opcode in [1, 2, 5, 6, 7, 8]:
            parameter_mode_1 = 0 if len(parameter_modes) < 1 else int(parameter_modes[len(parameter_modes) - 1])
            parameter_1 = int(program[i + 1]) if parameter_mode_1 == 1 else program[program[i + 1]]
            parameter_mode_2 = 0 if len(parameter_modes) < 2 else int(parameter_modes[len(parameter_modes) - 2])
            parameter_2 = int(program[i + 2]) if parameter_mode_2 == 1 else program[program[i + 2]]
            instruction_length = 3
            if log:
                instruction += ', ' + str(program[i + 2])
            if opcode in [1, 2, 7, 8]:
                parameter_3 = program[i + 3]
                instruction_length = 4
                if log:
                    instruction += ', ' + str(program[i + 3])
        if log:
            print('Opcode: ' + str(opcode) + ' at position ' + str(i) + '; parameter modes: ' + parameter_modes + ' (instr: ' + instruction + ')')
        if opcode == 1:
            # Add parameters
            if log:
                print('Adding: ', parameter_1, parameter_2)
            program[parameter_3] = int(parameter_1) + int(parameter_2)
        elif opcode == 2:
            # Multiply parameters
            if log:
                print('Multiplying: ', parameter_1, parameter_2)
            program[parameter_3] = int(parameter_1) * int(parameter_2)
        elif opcode == 3:
            # Ask for input integer and store it
            val = input_1 if input_count == 1 else input_2
            position = program[i + 1]
            program[position] = val
            input_count += 1
        elif opcode == 4:
            # Output integer
            parameter = program[i + 1]
            output = parameter if int(parameter_modes[len(parameter_modes) - 1]) == 1 else program[parameter]
            return output
        elif opcode == 5:
            # Jump-if-true
            if parameter_1 != 0:
                i = parameter_2
                continue # Avoid the pointer increment at the end of this loop
        elif opcode == 6:
            # Jump-if-false
            if parameter_1 == 0:
                i = parameter_2
                continue # Avoid the pointer increment at the end of this loop
        elif opcode == 7:
            # Less-than
            program[parameter_3] = 1 if int(parameter_1) < int(parameter_2) else 0
        elif opcode == 8:
            # Equals
            program[parameter_3] = 1 if int(parameter_1) == int(parameter_2) else 0
        elif opcode == 99:
            # End program
            if log:
                print('Ending program!')
            quit()
        i += instruction_length
    return program

def run_amp(phase, input):
    return run(input_data, phase, input)

def calculate_output_signal(phases):
    input = 0
    for phase in phases:
        input = run_amp(phase, input)
    return input

def find_highest_output_signal():
    phases_list = list(itertools.permutations([0, 1, 2, 3, 4]))
    output_signals = []
    for phases in phases_list:
        output_signals.append(calculate_output_signal(phases))
    return max(output_signals)

print(find_highest_output_signal())