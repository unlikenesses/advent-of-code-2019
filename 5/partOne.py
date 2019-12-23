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

def run(program, log = False):
    program = program[:] # Copy mutable list to avoid overriding it
    length = len(program)
    i = 0
    while i < length:
        instruction_length = 2
        if log:
            instruction = str(program[i]) + ', ' + str(program[i + 1])
        parsed = parse_parameter_mode_and_opcode(program[i])
        opcode = parsed['opcode']
        parameter_modes = str(parsed['parameter_modes'])
        if opcode in [1, 2]:
            parameter_mode_1 = 0 if len(parameter_modes) < 1 else int(parameter_modes[len(parameter_modes) - 1])
            parameter_1 = int(program[i + 1]) if parameter_mode_1 == 1 else program[program[i + 1]]
            parameter_mode_2 = 0 if len(parameter_modes) < 2 else int(parameter_modes[len(parameter_modes) - 2])
            parameter_2 = int(program[i + 2]) if parameter_mode_2 == 1 else program[program[i + 2]]
            parameter_3 = program[i + 3]
            instruction_length = 4
            if log:
                instruction += ', ' + str(program[i + 2]) + ', ' + str(program[i + 3])
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
            val = input('Speak to me: ')
            position = program[i + 1]
            program[position] = val
        elif opcode == 4:
            # Output integer
            parameter = program[i + 1]
            output = parameter if int(parameter_modes[len(parameter_modes) - 1]) == 1 else program[parameter]
            print('OUTPUT: ' + str(output))
        elif opcode == 99:
            # End program
            if log:
                print('Ending program!')
            quit()
        i += instruction_length
    return program

run(input_data, True)