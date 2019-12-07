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
    name_objects = []
    #slice string on eithe side of the ')'
    for index, pair in enumerate(array):
        parens_index = pair.index(')')
        #append the first pair as they are guaranteed unique
        if index == 0:
            orbitee = Object(pair[:parens_index])
            orbiter = Object(pair[parens_index+1:])

            objects.append(orbitee)
            objects.append(orbiter)

            name_objects.append(orbitee.name)
            name_objects.append(orbiter.name)
        #check for unique pairs
        else:
            #find the existing object in the list or the direct orbit and
            #establish the linked list
            orbitee = Object(pair[:parens_index])
            orbiter = Object(pair[parens_index+1:])


            if orbitee.name not in name_objects:
                objects.append(orbitee)
                name_objects.append(orbitee.name)
            if orbiter.name not in name_objects:
                objects.append(orbiter)
                name_objects.append(orbiter.name)


    return objects

def create_graph(objects_array, orbits_array):
    """
    create the linked list by connecting each objects direct_orbit member
    """
    for index, pair in enumerate(orbits_array):
        parens_index = pair.index(')')


        orbitee = str(pair[:parens_index])
        orbiter = str(pair[parens_index+1:])

        for x in objects_array:
            if x.name == orbitee:
                object_orbitee = x
                break
        for x in objects_array:
            if x.name == orbiter:
                object_orbiter = x
                break

        object_orbiter.direct_orbit = object_orbitee

        #pop the pair to shorten the list for the larger input?



def main():
    output = read_input()
    list_objects = create_objects(output)

    create_graph(list_objects, output)



    total_orbits = 0
    for item in list_objects:
        cursor = item.get_direct_orbits()
        while cursor:
            total_orbits += 1
            cursor = cursor.direct_orbit

    print(total_orbits)

if __name__ == "__main__":
    main()
