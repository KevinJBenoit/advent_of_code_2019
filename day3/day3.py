import csv
import os




def organize_csv(file):
    """
    read in the csv file and organize the rows into dictionary variables
    """
    os.chdir(r'C:\Users\Kevin Benoit\OneDrive\Code\AdventOfCode2019\day3')

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
    path = [[0, 0]]
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

    #translate the endpoints into lines
    lines = []
    directions = []
    for index in range(len(path)):
        if index == len(path)-1:
            break
        else:
            lines.append([path[index], path[index+1]])
            directions.append(find_direction([path[index], path[index+1]]))

    return lines, directions


def find_direction(line):
    if line[0][0] == line[1][0]:
        return 'vertical'
    else:
        return 'horizontal'

def find_intersections(traversal1, traversal2):
    """
    returns a list of x,y coordinates where there is overlap between the two wires
    """
    intersections = []

    return intersections

def path_coordinates(line, wire_in):
    direction = wire_in[0]
    #CREATE A FOR LOOP TO LOOP THROUGH ALL LINES FIX THIS UP
    path = [line[0]]
    cursor = line[0].copy()

    for i in range(wire_in[1]):
        if direction == 'U':
            cursor[1] += 1
            path.append(cursor.copy())

        #moves down, subtract from y
        elif direction == 'D':
            cursor[1] -= 1
            path.append(cursor.copy())

        #moves left, subtract from x
        elif direction == 'L':
            cursor[0] -= 1
            path.append(cursor.copy())

        #moves right, add to x
        elif direction == 'R':
            cursor[0] += 1
            path.append(cursor.copy())

    return path

def main():
    """
    This was a tough one
    """
    wire1, wire2 = organize_csv('wire_input.txt')

    path1, directions1 = translate_traversal(wire1)
    path2, directions2 = translate_traversal(wire2)

    coordinates1 = []
    coordinates2 = []
    intersect = []

    for index, line in enumerate(path1):
        coordinates1.append(path_coordinates(line, wire1[index]).copy())

    for index, line in enumerate(path2):
        coordinates2.append(path_coordinates(line, wire2[index]).copy())

    steps1 = []
    steps2 = []

    #these are the intersections found from part1
    #I used a nested loops to brute force the intersections, saved the output in
    for index1, line1 in enumerate(path1):
        step1 += wire1[index1][1]
        print(step1)
        for index2, line2 in enumerate(path2):
            step2 += path2[index2]
            #check the orientation of lines to reduce number of computations
            if directions1[index1] != directions2[index2]:
                for point in coordinates1[index1]:
                    if point in coordinates2[index2]:
                        steps1.append(step1)
                        steps2.append(step2)
                        intersect.append(point)

    #saved the intersect variable so i didn't have to compute it all over again for part2
    intersctions = [[-904, 1465], [-309, 1465], [-904, 1227], [-309, 1227], [-309, 1636], [-309, 1701], [-309, 1021], [-727, 1719], [-359, 725], [-309, 1612], [-458, 1719], [-904, 1475], [-904, 1456], [-309, 1185], [-505, 1719], [-904, 1211], [-1984, 1177], [-1978, 1423], [-501, 1719], [-309, 1503]]



    #increment the steps until the line containing the first intersection for both wires
    for i in range(8):
        steps1 += wire1[i][1]
    for i in range(7):
        steps2 += wire2[i][1]

    #add in the final wire1 until the intersection point is reached
    for intersect in intersctions:
        if intersect in coordinates2[7]:
            print(coordinates2[7].index(intersect))

    #add in the final wire2 until the intersection point is reached
    for intersect in intersctions:
        if intersect in coordinates1[8]:
            print(coordinates1[8].index(intersect))

    #added the final wires to their respective steps
    step1 += 671
    step2 += 677
    #print the combined steps
    print(steps1 + steps2)
if __name__ == "__main__":
    main()
