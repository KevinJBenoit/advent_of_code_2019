from puzzle_input_day11 import intcode


def compute_opcodes(codes, program_list, program_dict, instruction_pointer, relative_base, auto_input=None):
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
        return False, None

    if position_0 == 1:
        if instructions:
            add_opcode(codes, program_list, program_dict, instructions, relative_base)
        else:
            add_opcode(codes, program_list, program_dict)

    elif position_0 == 2:
        if instructions:
            multiply_opcode(codes, program_list, program_dict, instructions, relative_base)
        else:
            multiply_opcode(codes, program_list, program_dict)

    #if position 3 only use 2 codes
    elif position_0 == 3:
        if instructions:
            take_input(codes, program_list, program_dict, relative_base, auto_input, instructions)
        else:
            take_input(codes, program_list, program_dict, relative_base, auto_input)

    elif position_0 == 4:
        if instructions:
            output = output_parameter(codes, program_list, program_dict, instructions, relative_base)
        else:
            output = output_parameter(codes, program_list, program_dict)
        return True, output

    elif position_0 == 5:
        jump_if_true(codes, program_list, program_dict, instructions, instruction_pointer, relative_base)

    elif position_0 == 6:
        jump_if_false(codes, program_list, program_dict, instructions, instruction_pointer, relative_base)

    elif position_0 == 7:
        less_than(codes, program_list, program_dict, instructions, relative_base)

    elif position_0 == 8:
        equals(codes, program_list, program_dict, instructions, relative_base)

    elif position_0 == 9:
        adjust_relative_base(codes, program_list, program_dict, relative_base, instructions)

    return True, None

def add_opcode(codes, program_list, program_dict, instructions=None, relative_base=None):
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
            position_1 = program_list[relative_base[0] + codes[1]]
        else:
            position_1 = program_list[codes[1]]

        #find mode of position 2
        if instructions[1] == 1:
            position_2 = codes[2]
        elif instructions[1] == 2:
            position_2 = program_list[relative_base[0] + codes[2]]
        else:
            position_2 = program_list[codes[2]]

        #find mode of position 3
        if instructions[2] == 1:
             print("add opcode position 3 should not be in immediate mode!")
        if instructions[2] == 2:
            position_3 = relative_base[0] + codes[3]
        else:
            position_3 = codes[3]

    else:
        try:
            position_1 = program_list[codes[1]]
        except:
            position_1 = 0
        try:
            position_2 = program_list[codes[2]]
        except:
            position_2 = 0

        position_3 = codes[3]
    try:
        program_list[position_3] = position_1 + position_2
    except:
        program_dict.update({position_3: position_1 + position_2})


def multiply_opcode(codes, program_list, program_dict, instructions=None, relative_base=None):
    """
    protocol if position 0 is a 1, adds elements found at positions 2 and 3
    indicators, their product is stored at position 3 indicator
    """
    if instructions:
        #find mode of position 1
        if instructions[0] == 1:
            position_1 = codes[1]
        elif instructions[0] == 2:
            position_1 = program_list[relative_base[0] + codes[1]]
        else:
            position_1 = program_list[codes[1]]

        #find mode of position 2
        if instructions[1] == 1:
            position_2 = codes[2]
        elif instructions[1] == 2:
            position_2 = program_list[relative_base[0] + codes[2]]
        else:
            position_2 = program_list[codes[2]]

        #find mode of position 3
        if instructions[2] == 1:
             print("multiply opcode position 3 should not be in immediate mode!")
        if instructions[2] == 2:
            position_3 = relative_base[0] + codes[3]
        else:
            position_3 = codes[3]

    else:
        position_1 = program_list[codes[1]]
        position_2 = program_list[codes[2]]
        position_3 = codes[3]
    try:
        program_list[position_3] = position_1 * position_2
    except:
        program_dict.update({position_3: position_1 * position_2})


def take_input(codes, program_list, program_dict, relative_base=None, auto_input=None, instructions=None):
    """
    protocol if position 0 is a 3, will ask for an integer input value from user
    and store it at the address provided by position 1
    """
    if instructions:
        if instructions[0] == 1:
            position_1 = codes[1]
        elif instructions[0] == 2:
            position_1 = relative_base[0] + codes[1]

    else:
        position_1 = codes[1]

    integer_input_value = auto_input
    program_list[position_1] = integer_input_value

def output_parameter(codes, program_list, program_dict, instructions=None, relative_base=None):
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
            # print(output)
            # program_list[0] = output
            return output
    else:
        position_1 = codes[1]

    output = program_list[position_1]

    # # print(output)

    # program_list[0] = output
    return output

def jump_if_true(codes, program_list, program_dict, instructions, instruction_pointer, relative_base=None):
    """
    if the first parameter is non-zero, it sets the instruction pointer to the
    value from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program_list[relative_base[0] + codes[1]]
        else:
            first_parameter = program_list[codes[1]]

        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program_list[relative_base[0] + codes[2]]
        else:
            second_parameter = program_list[codes[2]]

        third_parameter = codes[3]

    else:
        first_parameter = program_list[codes[1]]
        second_parameter = program_list[codes[2]]
        third_parameter = codes[3]


    if first_parameter != 0:
        instruction_pointer[0] = second_parameter
    else:
        instruction_pointer[0] += 3

def jump_if_false(codes, program_list, program_dict, instructions, instruction_pointer, relative_base=None):
    """
    if the first parameter is zero, it sets the instruction pointer to the value
    from the second parameter. Otherwise, it does nothing.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program_list[relative_base[0] + codes[1]]
        else:
            first_parameter = program_list[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program_list[relative_base[0] + codes[2]]

        else:
            second_parameter = program_list[codes[2]]

        third_parameter = codes[3]

    else:
        first_parameter = program_list[codes[1]]
        second_parameter = program_list[codes[2]]
        third_parameter = codes[3]

    if first_parameter == 0:
        instruction_pointer[0] = second_parameter
    else:
        instruction_pointer[0] += 3

def less_than(codes, program_list, program_dict, instructions, relative_base=None):
    """
    if the first parameter is less than the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program_list[relative_base[0] + codes[1]]
        else:
            first_parameter = program_list[codes[1]]
        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program_list[relative_base[0] + codes[2]]
        else:
            second_parameter = program_list[codes[2]]
        if instructions[2] == 2:
            third_parameter = relative_base[0] + codes[3]
        else:
            third_parameter = codes[3]

        #logic test operation
        if first_parameter < second_parameter:
            program_list[third_parameter] = 1
        else:
            program_list[third_parameter] = 0

    else:
        first_parameter = program_list[codes[1]]
        second_parameter = program_list[codes[2]]
        third_parameter = codes[3]

        #logic test operation
        if first_parameter < second_parameter:
            program_list[third_parameter] = 1
        else:
            program_list[third_parameter] = 0


def equals(codes, program_list, program_dict, instructions, relative_base=None):
    """
    if the first parameter is equal to the second parameter, it stores 1 in the
    position given by the third parameter. Otherwise, it stores 0.
    """

    if instructions:
        if instructions[0] == 1:
            first_parameter = codes[1]
        elif instructions[0] == 2:
            first_parameter = program_list[relative_base[0] + codes[1]]
        else:
            first_parameter = program_list[codes[1]]

        if instructions[1] == 1:
            second_parameter = codes[2]
        elif instructions[1] == 2:
            second_parameter = program_list[relative_base[0] + codes[2]]
        else:
            second_parameter = program_list[codes[2]]

        if instructions[2] == 2:
            third_parameter = relative_base[0] + codes[3]
        else:
            third_parameter = codes[3]

        #logic test operation
        if first_parameter == second_parameter:
            program_list[third_parameter] = 1
        else:
            program_list[third_parameter] = 0

    else:
        first_parameter = program_list[codes[1]]
        second_parameter = program_list[codes[2]]
        third_parameter = codes[3]

        #logic test operation
        if first_parameter == second_parameter:
            program_list[third_parameter] = 1
        else:
            program_list[third_parameter] = 0


def adjust_relative_base(codes, program_list, program_dict, relative_base, instructions):
    """
    permanently adjusts the relative base to the value indicated by its only
    parameter
    """
    if instructions:
        parameter_1 = instructions[0]
        if parameter_1 == 1:
            relative_base[0] += codes[1]

        elif parameter_1 == 2:
            relative_base[0] += program_list[relative_base[0] + codes[1]]
    else:
        relative_base[0] += program_list[codes[1]]


def program_output(list_intcode, dict_intcode, instruction_pointer, base_wrapper, input_from_camera):
    """
    produces the output of the program_list with the given noun and verb
    """

    flag = True
    i = 0
    pointer_wrapper = [instruction_pointer[0]]
    relative_base = [base_wrapper[0]]
    #slice through the program_list 4 codes at a time
    #if position 0 is 3, slice 2 codes
    while flag:
        i = pointer_wrapper[0]
        opcode = dict_intcode[i]
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
            flag, output = compute_opcodes(list_intcode[0+i:2+i], list_intcode, dict_intcode, pointer_wrapper, relative_base, input_from_camera)
            pointer_wrapper[0] += 2

            if opcode == 4:
                instruction_pointer[0] = pointer_wrapper[0]
                base_wrapper[0] = relative_base[0]
                return output, True

        #jump codes, i is moved according to them
        elif opcode == 5 or opcode == 6:
            #i is not being modified inside the function
            flag, output = compute_opcodes(list_intcode[0+i:4+i], list_intcode, dict_intcode, pointer_wrapper, relative_base)
        #compute the next 4 codes
        else:
            flag, output = compute_opcodes(list_intcode[0+i:4+i], list_intcode, dict_intcode, pointer_wrapper, relative_base)
            pointer_wrapper[0] += 4

    list_intcode[0] = 99
    instruction_pointer[0] = pointer_wrapper[0]
    base_wrapper[0] = relative_base[0]
    return list_intcode[0], False

class Hull:
    def __init__(self, size, robot):
        self.size = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.robot = robot

    def print_hull(self):
        """
        print out the state of the hull
        """
        fileout = open("output.txt", 'w')

        for y in range(self.size):
            for x in range(self.size):
                if x == self.robot.x and y == self.robot.y:
                    if self.robot.direction == 'n':
                        print('^', file=fileout, end=' ')
                    elif self.robot.direction == 'e':
                        print('>', file=fileout,end=' ')
                    elif self.robot.direction == 's':
                        print('v', file=fileout, end=' ')
                    elif self.robot.direction == 'w':
                        print('<', file=fileout, end=' ')
                else:
                    if self.matrix[y][x] == 0:
                        print('.', file=fileout, end=' ')
                    else:
                        print('#', file=fileout, end=' ')
            print(file=fileout)
        print(file=fileout)

    def robot_start(self):
        """
        sets the initial position of the robot to a white space
        """
        self.matrix[self.robot.y][self.robot.x] = 1

class Robot:
    def __init__(self, intcode_program, position):
        self.dict_intcode = {i: value for i, value in enumerate(intcode_program)}
        self.list_intcode = intcode_program
        self.instruction_pointer = [0]
        self.relative_base = [0]
        self.position_xy = f"{position[0]},{position[1]}"
        self.x = position[0]
        self.y = position[1]
        self.direction = 'n'
        self.current_color = 0
        self.unique_paint= []
        self.count = 0
    def take_picture(self, hull):
        """
        returns the value of the space the robot is currently occupying
        """
        return hull.matrix[self.y][self.x] #PROBLEM HERE????????????????????????????????

    def move(self, turn_direction):
        """
        input of 0 means it should turn left 90 degrees, and 1 means it should
        turn right 90 degrees
        directions represented by north, south, east, west
        """
        if turn_direction == 0:
            if self.direction == 'n':
                self.direction = 'w'

            elif self.direction == 'w':
                self.direction = 's'

            elif self.direction == 's':
                self.direction = 'e'

            elif self.direction == 'e':
                self.direction = 'n'

        if turn_direction == 1:
            if self.direction == 'n':
                self.direction = 'e'

            elif self.direction == 'e':
                self.direction = 's'

            elif self.direction == 's':
                self.direction = 'w'

            elif self.direction == 'w':
                self.direction = 'n'

        if self.direction == 'n':
            self.y -= 1
        elif self.direction == 'e':
            self.x += 1
        elif self.direction == 's':
            self.y += 1
        elif self.direction == 'w':
            self.x -= 1

        self.position_xy = f"{self.x},{self.y}"

    def paint(self, color, hull):
        """
        output a value indicating the color to paint the panel the robot is
        over: 0 means to paint the panel black, and 1 means to paint the panel
        white.
        """
        if self.position_xy not in self.unique_paint:
            self.unique_paint.append(self.position_xy)
            self.count += 1
        hull.matrix[self.y][self.x] = color

    def run_robot(self, hull):
        """
        robot uses it's internal intcode program as instructions
        input will be provided by it's camera from pictures of the hull
        output from the program will drive first: color to paint and second: movement
        """
        flag = True
        while flag:

            intcode_input = self.take_picture(hull)
            paint_color, flag = program_output(self.list_intcode, self.dict_intcode, self.instruction_pointer, self.relative_base, intcode_input)
            movement, flag = program_output(self.list_intcode, self.dict_intcode, self.instruction_pointer, self.relative_base, intcode_input)

            self.paint(paint_color, hull)
            self.move(movement)
        hull.print_hull()

def main():
    """
    main
    """
    #quick and dirty way of extending memory
    for i in range(1000):
        intcode.append(0)


    size = 400
    starting_position = [size//2, size//2]

    #initialize robot and hull
    robot = Robot(intcode, starting_position)
    ship_hull = Hull(size, robot)
    ship_hull.robot_start()

    robot.run_robot(ship_hull)


if __name__ == "__main__":
    main()
