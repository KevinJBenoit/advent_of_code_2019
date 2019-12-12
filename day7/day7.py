from puzzle_input_day7 import intcode
import itertools

def compute_opcodes(codes, program, instruction_pointer, input_values=None):
    """
    performs the math operations on the program
    """

    instructions = None
    #if there is a parameter mode
    if codes[0] > 99:
        #break down the parameters
        list_parameter = [int(digit) for digit in str(codes[0])]
        length_of_instruction = len(list_parameter)
        #check if there is a 2nd parameter
        if length_of_instruction == 3:
            #DE
            two_digit_opcode = list_parameter[1:]
            #C
            first_parameter = list_parameter[0]
            #B
            second_parameter = 0
            #A
            third_parameter = 0

        #check if there is a 3nd parameter
        elif length_of_instruction == 4:
            #DE
            two_digit_opcode = list_parameter[2:]
            #C
            first_parameter = list_parameter[1]
            #B
            second_parameter = list_parameter[0]
            #A
            third_parameter = 0
        elif length_of_instruction == 5:
            #DE
            two_digit_opcode = list_parameter[3:]
            #C
            first_parameter = list_parameter[2]
            #B
            second_parameter = list_parameter[1]
            #A
            third_parameter = list_parameter[0]

        instructions = [first_parameter, second_parameter, third_parameter]


    #if there is an instruction, slice for the two digit opcode
    #change if OPCODES go larger than 9
    if codes[0] > 99:
        position_0 = two_digit_opcode[1]
    else:
        position_0 = codes[0]


    if position_0 == 99:
        return False

    if position_0 == 1:
        if instructions:
            add_opcode(codes, program, instructions)
        else:
            add_opcode(codes, program)

    elif position_0 == 2:
        if instructions:
            multiply_opcode(codes, program, instructions)
        else:
            multiply_opcode(codes, program)

    #if position 3 only use 2 codes
    elif position_0 == 3:
        if input_values:
            take_input(codes, program, instruction_pointer, input_values)
        else:
            take_input(codes, program)

    elif position_0 == 4:
        output_parameter(codes, program)

    elif position_0 == 5:
        jump_if_true(codes, program, instructions, instruction_pointer)

    elif position_0 == 6:
        jump_if_false(codes, program, instructions, instruction_pointer)

    elif position_0 == 7:
        less_than(codes, program, instructions)

    elif position_0 == 8:
        equals(codes, program, instructions)

    return True

def add_opcode(codes, program, instructions=None):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their sum is stored at position 3 indicator
    """

    position_1 = None
    position_2 = None
    position_3 = None
    if instructions:
        if instructions[0] == 1:
            position_1 = codes[1]
        else:
            position_1 = program[codes[1]]
        if instructions[1] == 1:
            position_2 = codes[2]
        else:
            position_2 = program[codes[2]]
        position_3 = program[codes[3]]
    else:
        position_1 = program[codes[1]]
        position_2 = program[codes[2]]
        position_3 = program[codes[3]]

    program[codes[3]] = position_1 + position_2


def multiply_opcode(codes, program, instructions=None):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their product is stored at position 3 indicator
    """
    position_1 = None
    position_2 = None
    position_3 = None
    if instructions:
        if instructions[0] == 1:
            position_1 = codes[1]
        else:
            position_1 = program[codes[1]]
        if instructions[1] == 1:
            position_2 = codes[2]
        else:
            position_2 = program[codes[2]]

        position_3 = codes[3]
    else:
        position_1 = program[codes[1]]
        position_2 = program[codes[2]]
        position_3 = program[codes[3]]

    program[codes[3]] = position_1 * position_2


def take_input(codes, program, instruction_pointer=None, input_instructions=None):
    """
    protocol if position 0 is a 3, will ask for an integer input value from user
    and store it at the address provided by position 1
    """
    if input_instructions:
        #if first input, then its the phase signal
        if instruction_pointer[0] == 0:
            integer_input_value = input_instructions[0]
        #then its the second input instruction
        else:
            integer_input_value = input_instructions[1]

        position_1 = codes[1]
        program[position_1] = integer_input_value

    else:
        integer_input_value = int(input("Please provide an input: "))
        position_1 = codes[1]
        program[position_1] = integer_input_value


def output_parameter(codes, program):
    """
    protocol if position 0 is a 4, will immediately output the value that is stored
    at the address provided by position 1
    """
    position_1 = codes[1]

    output = program[position_1]

    program[0] = output
    return output

def jump_if_true(codes, program, instructions, instruction_pointer):
    """
    if the first parameter is non-zero, it sets the instruction pointer to the
    value from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        else:
            second_parameter = program[codes[2]]

        third_parameter = codes[3]

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]


    if first_parameter != 0:
        instruction_pointer[0] = second_parameter
    else:
        instruction_pointer[0] += 3

def jump_if_false(codes, program, instructions, instruction_pointer):
    """
    if the first parameter is zero, it sets the instruction pointer to the value
    from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        else:
            second_parameter = program[codes[2]]

        third_parameter = codes[3]

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]

    if first_parameter == 0:
        instruction_pointer[0] = second_parameter
    else:
        instruction_pointer[0] += 3

def less_than(codes, program, instructions):
    """
    if the first parameter is less than the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        else:
            second_parameter = program[codes[2]]

        third_parameter = codes[3]

        if first_parameter < second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]

        if first_parameter < second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0


def equals(codes, program, instructions):
    """
    if the first parameter is equal to the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        else:
            second_parameter = program[codes[2]]

        third_parameter = codes[3]

        if first_parameter == second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]

        if first_parameter == second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0

def program_output(intcode_in, phase_value, input_signal):
    """
    produces the output of the program with the given noun and verb
    """
    #instructions for automating the amplifier inputs
    input_instructions = [phase_value, input_signal]

    list_intcode = list(intcode_in)
    flag = True
    i = 0
    wrapper = [0,]
    #slice through the program 4 codes at a time
    #if position 0 is 3, slice 2 codes
    while flag:
        i = wrapper[0]
        opcode = list_intcode[0+i]
        #handle paramemter mode
        if opcode > 99:
            list_opcode = [int(digit) for digit in str(opcode)]

            #only get the opcode from the parameter mode
            if len(list_opcode) == 3:
                list_opcode = list_opcode[1:]
            elif len(list_opcode) == 4:
                list_opcode = list_opcode[2:]

            final_list_opcode = [str(digit) for digit in list_opcode]
            opcode = int("".join(final_list_opcode))


        if opcode == 3 or opcode == 4:
            flag = compute_opcodes(list_intcode[0+i:2+i], list_intcode, wrapper, input_instructions)
            wrapper[0] += 2
        #jump codes, i is moved according to them
        elif opcode == 5 or opcode == 6:
            #i is not being modified inside the function
            flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode, wrapper)
        #compute the next 4 codes
        else:
            flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode, wrapper)
            wrapper[0] += 4

    return list_intcode[0]

def amplifier_control(phase_sequence, intcode_sequence):
    """
    runs the amplifier software using the given phase sequence
    returns the thruster signal strength
    """
    input_signal = None
    for index, phase in enumerate(phase_sequence):
        if index == 0:
            input_signal = 0
            input_signal = program_output(intcode_sequence, phase, input_signal)
        else:
            input_signal = program_output(intcode_sequence, phase, input_signal)

    thruster_signal = input_signal
    return thruster_signal

def main():
    """
    Copied over code from Day 2 for modification
    """
    phase_setting_sequence = [0,1,2,3,4]
    thruster_signals = []
    permutations = list(itertools.permutations(phase_setting_sequence))

    for sequence in permutations:
        thruster_signals.append(amplifier_control(sequence, intcode))

    print(max(thruster_signals))




if __name__ == "__main__":
    main()
