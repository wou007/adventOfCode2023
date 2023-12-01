import os

def ReadInput(day_number):
    filePath = ''
    if os.path.isfile('input.txt'):
        filePath = 'input.txt'
    elif os.path.isfile(f'Day{day_number}/input.txt'):
        filePath = f'Day{day_number}/input.txt'
    
    file = open(filePath, 'r')
    data = file.read()
    file.close()

    return data

def Create2DList(width,height,initValue = 0):
    result = []
    for i in range(height):
        result.append([initValue for j in range(width)])
    return result

def Print2dList(list):
    for row in list:
        txt = ''
        for point in row:
            txt = txt + str(point)
        print(txt)