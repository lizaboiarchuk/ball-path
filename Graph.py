from Node import *
from Matrix import *


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.graph = self.build_graph()
        self.cost = 1  # we will define cost '1' for all movements, because they are equal
        self.moves = {(1, 0): 'D',
                      (-1, 0): 'U',
                      (0, -1): 'L',
                      (0, 1): 'R'}

    # get the neighbours of given cell
    def neighbours(self, position):
        neighouhrs = []
        i = position[0]
        j = position[1]
        if i - 1 >= 0 and self.matrix.values[i - 1][j] != 1:
            neighouhrs.append((i - 1, j))
        if i + 1 < self.matrix.height and self.matrix.values[i + 1][j] != 1:
            neighouhrs.append((i + 1, j))
        if j - 1 >= 0 and self.matrix.values[i][j - 1] != 1:
            neighouhrs.append((i, j - 1))
        if j + 1 < self.matrix.width and self.matrix.values[i][j + 1] != 1:
            neighouhrs.append((i, j + 1))
        return neighouhrs

    # initialize the graph from matrix
    def build_graph(self):
        graph = {}
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if self.matrix.values[i][j] == 0:
                    graph[(i, j)] = self.neighbours((i, j))
        return graph

    # A-STAR search with given heuristic
    def search(self, start_position, end_position, heuristic):
        self.graph[start_position] = self.neighbours(start_position)
        start_node = Node(None, start_position)
        end_node = Node(None, end_position)
        start_node.g = end_node.g = 0
        start_node.h = end_node.h = 0
        start_node.f = end_node.f = 0
        open = []
        closed = []
        open.append(start_node)

        while not len(open) == 0:
            open.sort()
            current_node = open.pop(0)
            closed.append(current_node.position)

            if (current_node.position == end_node.position):
                return current_node.path()

            children = self.graph[current_node.position]
            for child_position in children:
                if child_position in closed:
                    continue
                child = Node(current_node, child_position)
                child.g = current_node.g + self.cost
                child.h = heuristic(child.position, end_node.position)
                child.f = child.g + child.h
                for node in open:
                    if child_position == node.position and child.g > node.g:
                        continue
                open.append(child)

    # dictionary with path positions and their directions (U, D, L, R)
    def directions(self, path):
        directions = {}
        current = path[-1]
        directions[current.position] = 'F'
        while current.parent != None:
            dir = (current.position[0] - current.parent.position[0], current.position[1] - current.parent.position[1])
            directions[current.parent.position] = self.moves[dir]
            current = current.parent
        return directions

    # matrix with path direction letters ('u', 'd', 'l','r') and 'balls' ('o')
    def path_matrix(self, path):
        directions = self.directions(path)
        new_matrix_values = []
        for i in range(self.matrix.height):
            row = []
            for j in range(self.matrix.width):
                if (i, j) in list(map(lambda x: x.position, path)):
                    row.append(directions[(i, j)])
                elif self.matrix.values[i][j] == 1:
                    row.append('o')
                else:
                    row.append(' ')
            new_matrix_values.append(row)
        new_matrix = Matrix(self.matrix.height, self.matrix.width, new_matrix_values)
        return new_matrix
