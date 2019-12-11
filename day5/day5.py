from puzzle_input_day5 import intcode


def compute_opcodes(codes, program):
    """
    performs the math operations on the program
    """
    #there is a parameter mode
    instructions = None
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
        take_input(codes, program)

    elif position_0 == 4:
        print(output_parameter(codes, program))

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

def take_input(codes, program):
    """
    protocol if position 0 is a 3, will ask for an integer input value from user
    and store it at the address provided by position 1
    """
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

    return output


def parameter_mode(parameters, codes, program):
    """
    takes the ABCDE paraemters and performs proper computations
    """
    #break down the parameters
    list_parameter = [int(digit) for digit in str(parameters)]
    length_of_instruction = len(list_parameter)
    #check if there is a 2nd parameter
    if length_of_instruction == 3:
        #DE
        two_digit_opcode = list_parameter[1:]
        #C
        first_parameter = list_parameter[0]
        #B
        second_parameter = None
        #A
        third_parameter = None

    #check if there is a 3nd parameter
    elif length_of_instruction == 4:
        #DE
        two_digit_opcode = list_parameter[2:]
        #C
        first_parameter = list_parameter[1]
        #B
        second_parameter = list_parameter[0]
        #A
        third_parameter = None
    elif length_of_instruction == 5:
        #DE
        two_digit_opcode = list_parameter[3:]
        #C
        first_parameter = list_parameter[2]
        #B
        second_parameter = list_parameter[1]
        #A
        third_parameter = list_parameter[0]

    if two_digit_opcode == 99:
        return False



    return True
def program_output(intcode_in):
    """
    produces the output of the program with the given noun and verb
    """
    list_intcode = list(intcode_in)
    flag = True
    i = 0

    #slice through the program 4 codes at a time
    #if position 0 is 3, slice 2 codes
    while flag:
        if list_intcode[0+i] == 3 or list_intcode[0+i] == 4:
            flag = compute_opcodes(list_intcode[0+i:2+i], list_intcode)
            i += 2
        #compute the next 4 codes
        else:
            flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode)
            i += 4

    return list_intcode[0]



def main():
    """
    Copied over code from Day 2 for modification
    """

    output = program_output(intcode)

    print(output)


if __name__ == "__main__":
    main()
