from puzzle_input_day11 import intcode


def compute_opcodes(codes, program, instruction_pointer, relative_base):
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
            add_opcode(codes, program, instructions, relative_base)
        else:
            add_opcode(codes, program)

    elif position_0 == 2:
        if instructions:
            multiply_opcode(codes, program, instructions, relative_base)
        else:
            multiply_opcode(codes, program)

    #if position 3 only use 2 codes
    elif position_0 == 3:
        if instructions:
            take_input(codes, program, relative_base, instructions)
        else:
            take_input(codes, program, relative_base)

    elif position_0 == 4:
        if instructions:
            output_parameter(codes, program, instructions, relative_base)
        else:
            output_parameter(codes, program)

    elif position_0 == 5:
        jump_if_true(codes, program, instructions, instruction_pointer, relative_base)

    elif position_0 == 6:
        jump_if_false(codes, program, instructions, instruction_pointer, relative_base)

    elif position_0 == 7:
        less_than(codes, program, instructions, relative_base)

    elif position_0 == 8:
        equals(codes, program, instructions, relative_base)

    elif position_0 == 9:
        adjust_relative_base(codes, program, relative_base, instructions)

    return True

def add_opcode(codes, program, instructions=None, relative_base=None):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their sum is stored at position 3 indicator
    """

    position_1 = None
    position_2 = None
    position_3 = None
    if instructions:
        #find mode of position 1
        if instructions[0] == 1:
            position_1 = codes[1]
        elif instructions[0] == 2:
            position_1 = program[relative_base[0] + codes[1]]
        else:
            position_1 = program[codes[1]]

        #find mode of position 2
        if instructions[1] == 1:
            position_2 = codes[2]
        elif instructions[1] == 2:
            position_2 = program[relative_base[0] + codes[2]]
        else:
            position_2 = program[codes[2]]

        #find mode of position 3
        if instructions[2] == 1:
            position_3 = codes[2]
        elif instructions[2] == 2:
            position_3 = relative_base[0] + codes[3]
        else:
            position_3 = codes[3]

    else:
        position_1 = program[codes[1]]
        position_2 = program[codes[2]]
        position_3 = codes[3]

    program[position_3] = position_1 + position_2


def multiply_opcode(codes, program, instructions=None, relative_base=None):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their product is stored at position 3 indicator
    """
    if instructions:
        #find mode of position 1
        if instructions[0] == 1:
            position_1 = codes[1]
        elif instructions[0] == 2:
            position_1 = program[relative_base[0] + codes[1]]
        else:
            position_1 = program[codes[1]]

        #find mode of position 2
        if instructions[1] == 1:
            position_2 = codes[2]
        elif instructions[1] == 2:
            position_2 = program[relative_base[0] + codes[2]]
        else:
            position_2 = program[codes[2]]

        #find mode of position 3
        # if instructions[2] == 1:
        #     position_3 = codes[2]
        if instructions[2] == 2:
            position_3 = relative_base[0] + codes[3]
        else:
            position_3 = codes[3]

    else:
        position_1 = program[codes[1]]
        position_2 = program[codes[2]]
        position_3 = codes[3]

    program[position_3] = position_1 * position_2


#add RELATIVE BASE SUPPORT???????????????????????????????????????????????????????????
def take_input(codes, program, relative_base=None, instructions=None):
    """
    protocol if position 0 is a 3, will ask for an integer input value from user
    and store it at the address provided by position 1
    """
    if instructions:
        if instructions[0] == 2:
            position_1 = relative_base[0] + codes[1]

    else:
        position_1 = codes[1]

    integer_input_value = int(input("Please provide an input: "))
    program[position_1] = integer_input_value

#DO I NEED TO ADD INSTRUCTIONS + RELATIVE BASE TO 4????????????????????????????????????????
def output_parameter(codes, program, instructions=None, relative_base=None):
    """
    protocol if position 0 is a 4, will immediately output the value that is stored
    at the address provided by position 1
    """
    if instructions:
        if instructions[0] == 2:
            position_1 = relative_base[0] + codes[1]
        elif instructions[0] == 1:
            position_1 = codes[1]
            output = position_1
            print(output)
            return
    else:
        position_1 = codes[1]

    output = program[position_1]

    print(output)

    # program[0] = output
    # return output

def jump_if_true(codes, program, instructions, instruction_pointer, relative_base=None):
    """
    if the first parameter is non-zero, it sets the instruction pointer to the
    value from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program[relative_base[0] + codes[1]]
        else:
            first_parameter = program[codes[1]]

        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program[relative_base[0] + codes[2]]
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

def jump_if_false(codes, program, instructions, instruction_pointer, relative_base=None):
    """
    if the first parameter is zero, it sets the instruction pointer to the value
    from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program[relative_base[0] + codes[1]]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program[relative_base[0] + codes[2]]

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

def less_than(codes, program, instructions, relative_base=None):
    """
    if the first parameter is less than the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program[relative_base[0] + codes[1]]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program[relative_base[0] + codes[2]]
        else:
            second_parameter = program[codes[2]]
        if instructions[2] == 2:
            third_parameter = relative_base[0] + codes[3]
        else:
            third_parameter = codes[3]

        #logic test operation
        if first_parameter < second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]

        #logic test operation
        if first_parameter < second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0


def equals(codes, program, instructions, relative_base=None):
    """
    if the first parameter is equal to the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program[relative_base[0] + codes[1]]
        else:
            first_parameter = program[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program[relative_base[0] + codes[2]]
        else:
            second_parameter = program[codes[2]]
        if instructions[2] == 2:
            third_parameter = relative_base[0] + codes[3]
        else:
            third_parameter = codes[3]

        #logic test operation
        if first_parameter == second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0

    else:
        first_parameter = program[codes[1]]
        second_parameter = program[codes[2]]
        third_parameter = codes[3]

        #logic test operation
        if first_parameter == second_parameter:
            program[third_parameter] = 1
        else:
            program[third_parameter] = 0


def adjust_relative_base(codes, program, relative_base, instructions):
    """
    permanently adjusts the relative base to the value indicated by its only
    parameter
    """
    if instructions:
        parameter_1 = instructions[0]
        if parameter_1 == 1:
            relative_base[0] += codes[1]

        elif parameter_1 == 2:
            relative_base[0] += program[relative_base[0] + codes[1]]
    else:
        relative_base[0] += program[codes[1]]


def program_output(intcode_in):
    """
    produces the output of the program with the given noun and verb
    """
    #instructions for automating the amplifier inputs
    input_instructions = None
    list_intcode = list(intcode_in)
    flag = True
    i = 0
    pointer_wrapper = [0,]
    relative_base = [0,]
    #slice through the program 4 codes at a time
    #if position 0 is 3, slice 2 codes
    while flag:
        i = pointer_wrapper[0]
        opcode = list_intcode[0+i]
        #handle paramemter mode
        if opcode > 99:
            list_opcode = [int(digit) for digit in str(opcode)]

            #only get the opcode from the parameter mode
            if len(list_opcode) == 3:
                list_opcode = list_opcode[1:]
            elif len(list_opcode) == 4:
                list_opcode = list_opcode[2:]
            elif len(list_opcode) == 5:
                list_opcode = list_opcode[3:]

            final_list_opcode = [str(digit) for digit in list_opcode]
            opcode = int("".join(final_list_opcode))


        if opcode == 3 or opcode == 4 or opcode == 9:
            flag = compute_opcodes(list_intcode[0+i:2+i], list_intcode, pointer_wrapper, relative_base)
            pointer_wrapper[0] += 2


        #jump codes, i is moved according to them
        elif opcode == 5 or opcode == 6:
            #i is not being modified inside the function
            flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode, pointer_wrapper, relative_base)
        #compute the next 4 codes
        else:
            flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode, pointer_wrapper, relative_base)
            pointer_wrapper[0] += 4

    return list_intcode[0], False



def main():
    """
    main
    """
    #extend the intcode memory
    #todo: change up how additional memory is created to decrease runtime

    for i in range(100000):
        intcode.append(0)
    print(program_output(intcode))


if __name__ == "__main__":
    main()
