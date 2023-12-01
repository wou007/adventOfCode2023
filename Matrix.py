class Matrix():

    def __init__(self):
        self.matrix = None

    def Print(self):
        for row in self.matrix:
            txt = ''
            for point in row:
                txt = txt + str(point)
            print(txt)

    def FromInput(self, input):
        self.matrix = []
        
        for line in input:
            temp = []
            for c in line:
                temp.append(c)
            self.matrix.append(temp)

    def Generate(self, width, height, initValue):
        self.matrix = []
        for i in range(height):
            self.matrix.append([initValue for j in range(width)])

    def GetPixel(self, x, y):
        return self.matrix[y][x]

    def SetPixel(self, x, y, value):
        self.matrix[y][x] = value

    def IsCoordinateValid(self, x, y):
        result = False
        if  y >= 0:
            if x >= 0:
                result = True
        return result

    def GetNeighborsOf(self, x, y, diagonal=False):
        result = []

        if self.IsCoordinateValid(x - 1, y):
            result.append([x - 1, y])
        if self.IsCoordinateValid(x + 1, y):
            result.append([x + 1, y])
        if self.IsCoordinateValid(x, y - 1):
            result.append([x, y - 1])
        if self.IsCoordinateValid(x, y + 1):
            result.append([x, y + 1])

        if diagonal:
            if self.IsCoordinateValid(x - 1, y - 1):
                result.append([x - 1, y - 1])
            if self.IsCoordinateValid(x - 1, y + 1):
                result.append([x - 1, y + 1])
            if self.IsCoordinateValid(x + 1, y - 1):
                result.append([x + 1, y - 1])
            if self.IsCoordinateValid(x + 1, y + 1):
                result.append([x + 1, y + 1])

        return result
    
    def GetNeighborsOfWithValue(self, x, y, value, diagonal=False):
        result = []
        for n in self.GetNeighborsOf(x,y,diagonal):
            if self.GetPixel(n[0],n[1]) == value:
                result.append(n)

        return result
    
    def GetNeighborsOfWithNotValue(self, x, y, value, diagonal=False):
        result = []
        for n in self.GetNeighborsOf(x,y,diagonal):
            if self.GetPixel(n[0],n[1]) != value:
                result.append(n)

        return result

    def GetHeight(self):
        return len(self.matrix)
    
    def GetWidth(self):
        return len(self.matrix[0])
    
    def CountPixelsWithValue(self, value):
        result = 0
        for l in self.matrix:
            for i in l:
                if i == value:
                    result += 1
        return result
    
    def GetPixelsWithValue(self, value):
        result = []
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == value:
                    result.append([x,y])
        return result