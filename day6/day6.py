import os


def read_input():
    """
    read in a series of string numbers and return an equivalent list integers
    """
    current_path = os.path.dirname(__file__)
    new_path = current_path+r"\orbits.txt"

    infile = open(new_path, 'r')
    numbers = []
    for line in infile:
        line = line.rstrip()
        numbers.append(line)

    return numbers


class Object:
    def __init__(self, name):
        self.name = name
        self.total_orbits = 0
        self.direct_orbit = None

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

    def get_direct_orbits(self):
        return self.direct_orbit

    def get_orbits(self):
        return self.total_orbits


def create_objects(array):
    """
    create python objects from the array of string orbits
    returns array of objects
    """
    objects = []
    #slice string on eithe side of the ')'
    for index, pair in enumerate(array):
        parens_index = pair.index(')')
        #append the first pair as they are guaranteed unique
        if index == 0:
            orbitee = Object(pair[:parens_index])
            orbiter = Object(pair[parens_index+1:])

            objects.append(orbitee)
            objects.append(orbiter)

        #check for unique pairs
        else:
            #find the existing object in the list or the direct orbit and
            #establish the linked list
            orbitee = Object(pair[:parens_index])
            orbiter = Object(pair[parens_index+1:])

            #loop through the existing objects
            for thing in objects:
                if thing.name != orbitee.name:
                    objects.append(orbitee)

                if thing.name != orbiter.name:
                    objects.append(orbiter)



    return objects

def main():
    output = read_input()
    list_objects = create_objects(output)

    print(list_objects)

    # total_orbits = 0
    # for item in list_objects:
    #     cursor = item.get_direct_orbits()
    #     while cursor:
    #         total_orbits += 1
    #         cursor = cursor.direct_orbit


    # print(total_orbits)

if __name__ == "__main__":
    main()
