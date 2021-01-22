import sys
import re
from Graph import *
from heuristic import *


if __name__ == '__main__':

    # Getting data from text file, given as system argument
    # Default file - test1.txt

    path = "tests/test1.txt"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    file = open(path, 'r')


    # Getting info from file
    matrix_height = int(file.readline())
    matrix_width = int(file.readline())
    start_coordinates = re.findall(r'\d+', file.readline())
    start_position = (int(start_coordinates[0]), int(start_coordinates[1]))
    goal_coordinates = re.findall(r'\d+', file.readline())
    goal_position = (int(goal_coordinates[0]), int(goal_coordinates[1]))


    # reading matrix
    map = []
    for i in range(matrix_height):
        values = []
        line = file.readline().split()
        for value in line:
            values.append(int(value))
        map.append(values)
    matrix = Matrix(matrix_height, matrix_width, map)


    # Creating graph
    graph = Graph(matrix)
    heuristic = manhattan_distance
    path = graph.search(start_position, goal_position, heuristic) #getting path


    # Handling result
    if path == None:
        print("No path was found.")
    else:
        # Printing info about solution
        print(graph.path_matrix(path)) # print matrix with directions and balls
        directions_dict = graph.directions(path)
        directions = ""
        for move in path:
            if directions_dict[move.position] != 'F':
                directions+= directions_dict[move.position] + " -> "
            else:
                directions += directions_dict[move.position] + "."
        print("\n" + directions)
        print("\nPath length: " + str(len(path) - 1) + " steps.")