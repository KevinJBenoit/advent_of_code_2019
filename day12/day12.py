from puzzle_input_day12 import *
import itertools


def apply_gravity(moon_positions, moon_velocities):
    """
    consider every pair of moons, apply gravity for each pair,
    with each pair apply the results to their velocities
    """
    for pair in itertools.combinations(moon_positions, r=2):
        moon1_index = moon_positions.index(list(pair)[0])
        moon2_index = moon_positions.index(list(pair)[1])

        compare_positions(moon_positions[moon1_index], moon_velocities[moon1_index],
                          moon_positions[moon2_index], moon_velocities[moon2_index])

def apply_velocity(moon_positions, moon_velocities):
    """
    consider every moon, apply the velocity to its position
    """
    for index, moon_position in enumerate(moon_positions):
        for axis in moon_position:
            moon_position[axis] += moon_velocities[index][axis]

def compare_positions(moon1_position, moon1_velocity, moon2_position, moon2_velocity):
    """
    determine for each axis if the moon's velocity will increase or decrase by 1
    if they are the same nothing will happen
    """
    for axis in moon1_position:
        if moon2_position.get(axis) > moon1_position.get(axis):
            moon1_velocity[axis] += 1
            moon2_velocity[axis] -= 1
        elif moon2_position.get(axis) < moon1_position.get(axis):
            moon1_velocity[axis] -= 1
            moon2_velocity[axis] += 1
        else:
            continue

def get_system_total_energy(moon_positions, moon_velocities):
    """
    get the total energy of the system by adding together every moon's total energy
    total energy for a moon is its potential energy times its kinetic energy
    """
    total_energy = 0
    for index, moon in enumerate(moon_positions):
        potential_energy = 0
        kinetic_energy = 0
        for axis in moon:
            potential_energy += abs(moon[axis])
            kinetic_energy += abs(moon_velocities[index][axis])
        total_energy += potential_energy * kinetic_energy

    return total_energy

def main():
    """
    main
    """
    moon_positions = [io_position, europa_position, ganymede_position, callisto_position]
    moon_velocities = [io_velocity, europa_velocity, ganymede_velocity, callisto_velocity]
    steps = 0

    for i in range(1000):

        # for i in range(4):
        #     print(f"{moon_positions[i]} ----> {moon_velocities[i]}")

        apply_gravity(moon_positions, moon_velocities)
        apply_velocity(moon_positions, moon_velocities)
        steps += 1

        # print(f"After {steps} steps:")

        # for i in range(4):
        #     print(f"{moon_positions[i]} ----> {moon_velocities[i]}")

    print(get_system_total_energy(moon_positions, moon_velocities))

if __name__ == "__main__":
    main()