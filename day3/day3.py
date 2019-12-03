import csv
import os


def organize_csv(file, directory):
    """
    read in the csv file and organize the rows into dictionary variables
    """
    os.chdir(directory)

    #create containers for both rows
    tuples1 = []
    tuples2 = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        #set the cursor for the first set of data
        cursor = tuples1

        for row in csv_reader:
            for element in row:

                cursor.append((element[0], int(element[1:])))
            #switch the cursor to the second set of data
            cursor = tuples2

        return tuples1, tuples2


def translate_traversal(wire_in):
    """
    translate the traversal of the wire into x, y coordinate system
    """
    cursor = [0, 0]
    path = []
    for direction in wire_in:
        #moves up, adds to y
        if direction[0] == 'U':
            cursor[1] += direction[1]
            path.append(cursor.copy())

        #moves down, subtract from y
        elif direction[0] == 'D':
            cursor[1] -= direction[1]
            path.append(cursor.copy())

        #moves left, subtract from x
        elif direction[0] == 'L':
            cursor[0] -= direction[1]
            path.append(cursor.copy())

        #moves right, add to x
        elif direction[0] == 'R':
            cursor[0] += direction[1]
            path.append(cursor.copy())

    return path

def find_intersections(traversal1, traversal2):
    """
    returns a list of x,y coordinates where there is overlap between the two wires
    """
    intersections = []

    for coordinates in traversal1:
        if coordinates in traversal2:
            intersections.append(coordinates)

    return intersections


def main():
    #change the working directory to the day3 folder

    wire1, wire2 = organize_csv('wire_input.txt', './day3')

    path1 = translate_traversal(wire1)
    path2 = translate_traversal(wire2)

    intersections = find_intersections(path1, path2)

    print(path1)
    print(path2)
    print(intersections)

if __name__ == "__main__":
    main()
