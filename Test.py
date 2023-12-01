import Matrix

if __name__ == "__main__":
    matrix = Matrix.Matrix()
    matrix.Generate(5,5,'H')
    matrix.SetPixel(2,1,'A')
    matrix.SetPixel(3,3,'A')
    print(matrix.GetPixelsWithValue('A'))
    matrix.Print()