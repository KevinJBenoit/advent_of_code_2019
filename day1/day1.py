def read_input(file):
    """
    read in a series of string numbers and return an equivalent list integers
    """
    infile = open(file, 'r')
    numbers = []
    for line in infile:
        line = line.rstrip()
        numbers.append(int(line))

    return numbers


def fuel_counter_upper(mass):
    """
    divide mass by 3 and round down
    then subtract 2 to get the fuel
    """
    fuel = (mass // 3) - 2
    return fuel

def fuel_adjuster(module_fule):
    """

    """
    additional_fuel = fuel_counter_upper(module_fule)

    while additional_fuel >= 0:
        module_fule += additional_fuel
        additional_fuel = fuel_counter_upper(additional_fuel)

    return module_fule



def main():
    """
    main
    """
    #load and format the modules into integers
    modules = read_input("puzzle_input.txt")
    #calculate the fuel for each module
    fuel = [fuel_counter_upper(module) for module in modules]

    #sum the mass of all the fuels
    fuel_mass = sum(fuel)
    print(f"Before fuel adjustment: {fuel_mass}")

    #adjust for the weight of the fuels
    new_fuels = [fuel_adjuster(fuel_mass) for fuel_mass in fuel]

    #sum the new weight
    print(f"After fuel adjustment: {sum(new_fuels)}")

if __name__ == "__main__":
    main()
