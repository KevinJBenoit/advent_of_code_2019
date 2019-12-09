parameters = 1002

list_parameter = [int(digit) for digit in str(parameters)]
two_digit_opcode = list_parameter[2:]

first_parameter = list_parameter[1]
second_parameter = list_parameter[0]
print(list_parameter)
print(two_digit_opcode)

print(first_parameter)
print(second_parameter)