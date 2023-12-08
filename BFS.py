import Matrix
import queue

class BFSPath():
    def __init__(self, path) -> None:
        self.path = path

    def IsPixelInPath(self, pixel):
        return pixel in self.path
    
    def GetPath(self):
        return self.path
    
    def GetPathLen(self):
        return len(self.path)
    
    def GetCurrentPos(self):
        return self.path[-1]

class BFS():
    def __init__(self) -> None:
        self.map = None
        self.costMap = None
        self.startPixel = None
        self.endValue = None
        self.wall = '#'

    def SetMap(self, map):
        self.map = map
        self.costMap = Matrix.Matrix()
        self.costMap.Generate(map.GetWidth(),map.GetHeight(),None)

    def SetStartPixel(self, x, y):
        self.startPixel = [x, y]

    def SetStartPixelByValue(self, val):
        p = self.map.GetPixelsWithValue(val)
        if len(p) == 1:
            self.startPixel = p[0]
        else:
            raise Exception("More than one startpixel")
        
    def SetEndValue(self, end):
        self.endValue = end
        
    def SetWallValue(self, wall):
        self.wall = wall

    def CalculateShortestPath(self):
        tasks = queue.Queue()
        tasks.put(BFSPath([self.startPixel]))
        self.costMap.SetPixel(self.startPixel[0],self.startPixel[1],0)

        while not tasks.empty():
            t = tasks.get()
            currPos = t.GetCurrentPos()
            n = self.map.GetNeighborsOfWithNotValue(currPos[0],currPos[1],self.wall)
            for i in n:
                iVal = self.map.GetPixel(i[0],i[1])
                iCost = self.costMap.GetPixel(i[0],i[1])
                if iCost == None:
                    if iVal == self.endValue:
                        return t.GetPathLen()
                    self.costMap.SetPixel(i[0],i[1],t.GetPathLen())
                    p = t.GetPath().copy()
                    p.append(i)
                    tasks.put(BFSPath(p))