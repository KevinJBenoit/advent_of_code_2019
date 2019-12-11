import os
import math

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = [x, y]
        self.monitors = 0

        self.angles = []
        self.result = []
    def __str__(self):
        return f"{self.coordinates}, monitors {self.monitors}"

    def __repr__(self):
        return f"{self.coordinates}, monitors {self.monitors}"


    def gather_angles(self, asteroid_list):
        """
        given the list of other asteroids in the map, generate a list of angles
        to each one of them
        """
        x1 = self.x
        y1 = self.y
        for asteroid in asteroid_list:
            x2 = asteroid.x
            y2 = asteroid.y
            rise = y2 - y1
            run = x2-x1

            #get the angle between each asteroid
            angle = math.atan2(rise, run) * 180 / math.pi

            self.angles.append(angle)
        #if there are multiple angles, there is a blocking line of site with all
        #but 1
        for data in self.angles:
            if data not in self.result:
                self.result.append(data)
                self.monitors += 1


def load_data():
    """
    read in the image data from txt file
    """
    current_path = os.path.dirname(__file__)
    new_path = current_path+r"\map.txt"
    infile = open(new_path, 'r')
    data = []
    row = []
    for line in infile:
        row = []
        for point in line:
            if point == '\n':
                break
            else:
                row.append(point)
        data.append(row)
    return data

def generate_Asteroids(data):
    """
    generates a list of all asteroids on the map with x, y coordinates
    """
    asteroids = []
    for index_y, row in enumerate(data):
        for index_x, coordinate in enumerate(row):
            if coordinate == '#':
                asteroids.append(Asteroid(index_x, index_y))

    return asteroids


def main():
    """
    main
    """
    map_info = load_data()
    for line in map_info:
        print(line)

    asteroids = generate_Asteroids(map_info)

    for asteroid in asteroids:
        asteroid.gather_angles(asteroids)

    best_station = asteroids[0]

    for asteroid in asteroids:
        if asteroid.monitors > best_station.monitors:
            best_station = asteroid

    print(best_station)

if __name__ == "__main__":
    main()