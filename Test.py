import BFS
import Matrix

if __name__ == "__main__":
    matrix = Matrix.Matrix()
    matrix.FromInput(   "#######\n"+
                        "#S....#\n"+
                        "###...#\n"+
                        "#.....#\n"+
                        "#.#####\n"+
                        "#.....#\n"+
                        "###...#\n"+
                        "#.....#\n"+
                        "###...#\n"+
                        "#E....#\n"+
                        "#######\n")
    bfs = BFS.BFS()
    bfs.SetMap(matrix)
    bfs.SetStartPixelByValue('S')
    bfs.SetEndValue('E')
    print(bfs.CalculateShortestPath())