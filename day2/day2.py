from puzzle_input import intcode


def compute_opcodes(codes, program):
    """

    """
    position_0 = codes[0]
    # position_1 = codes[1]
    # position_2 = codes[2]
    # position_3 = codes[3]

    if position_0 == 99:
        return False

    if position_0 == 1:
        add_opcode(codes, program)

    elif position_0 == 2:
        multiply_opcode(codes, program)

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


def main():
    """
    main
    """
    list_intcode = list(intcode)


    flag = True
    i = 0
    #slice through the program 4 codes at a time
    while flag:
        flag = flag = compute_opcodes(list_intcode[0+i:4+i], list_intcode)
        i += 4

    print(list_intcode)


if __name__ == "__main__":
    main()
