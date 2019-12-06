from puzzle_input_day5 import intcode


def compute_opcodes(codes, program):
    """
    performs the math operations on the program
    """
    position_0 = codes[0]

    if position_0 == 99:
        return False

    if position_0 == 1:
        add_opcode(codes, program)

    elif position_0 == 2:
        multiply_opcode(codes, program)

    elif position_0 == 3:
        take_input(codes, program)

    elif position_0 == 4:
        output_parameter(codes, program)

    return True

def add_opcode(codes, program):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their sum is stored at position 3 indicator
    """
    position_1 = codes[1]
    position_2 = codes[2]
    position_3 = codes[3]

    program[position_3] = program[position_1] + program[position_2]


def multiply_opcode(codes, program):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their product is stored at position 3 indicator
    """
    position_1 = codes[1]
    position_2 = codes[2]
    position_3 = codes[3]

    program[position_3] = program[position_1] * program[position_2]


def program_output(intcode_in, noun, verb):
    """
    produces the output of the program with the given noun and verb
    """
    list_intcode = list(intcode_in)
    flag = True
    i = 0
    list_intcode[1] = noun
    list_intcode[2] = verb
    #slice through the program 4 codes at a time
    while flag:
        flag = flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode)
        i += 4

    return list_intcode[0]


def output_parameter(codes, program):
    return codes[1]

def take_input(codes, program):
    print("test")

def main():
    """
    Copied over code from Day 2 for modification
    """
    flag = False
    noun, verb = 0, 0

    while not flag:
        output = program_output(intcode, noun, verb)

        if output == 19690720:
            flag = True
        elif 19690720 - output < 99:
            verb = 19690720 - output
            flag = True
        else:
            noun += 1

    print(f"Output: {output}, noun: {noun}, verb:{verb}")
    print(f"Answer: {100 * noun + verb}")

if __name__ == "__main__":
    main()
