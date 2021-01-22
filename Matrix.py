class Matrix:

    def __init__(self, height, width, values):
        self.height = height
        self.width = width
        self.values = values


    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                res+= str(self.values[i][j]) + " "
            res+= "\n"
        return res

