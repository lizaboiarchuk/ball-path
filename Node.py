class Node:

    def __init__(self, parent=None, coordinates=None):
        self.parent = parent
        self.position = coordinates
        self.g = 0  # Cost from the start
        self.h = 0  # Estimated cost to the gosl
        self.f = 0  # Total cost to the neighbour

    # comparing two nodes
    def __lt__(self, other):
        return self.f < other.f

    # return the path from start position to this position
    def path(self):
        path = []
        cur = self
        while cur != None:
            path.append(cur)
            cur = cur.parent
        return path[::-1]
