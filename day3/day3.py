import csv
import os
from matplotlib import collections as mc
import matplotlib.pyplot as plt
import numpy as np



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
    for index in range(len(path)):
        if index == len(path)-1:
            break
        else:
            lines.append([path[index], path[index+1]])

    return lines


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

def path_coordinates(line):
    direction = find_direction(line)
    print(direction)


def main():

    wire1, wire2 = organize_csv('wire_input.txt')

    path1 = translate_traversal(wire1)
    path2 = translate_traversal(wire2)

    print(path1)



if __name__ == "__main__":
    main()
