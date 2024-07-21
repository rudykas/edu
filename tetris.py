import copy

line = [[1,1,1,1]]
ghe = [[1,1,1], [0,0,1]]

def print_piece(piece):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            print(piece[i][j], end = '')
        print()

# print_piece(ghe)

def print_stakan_inc(x,y):
    array = [0]*x
    return copy.deepcopy([array]*y)

def print_stakan(x,y):
    return [[0]*x for i in range(y)]

stakan5_10 = print_stakan(5,10)

def projection(x,y, piece, array):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            array[i+y][j+x] = piece[i][j]
    return array

print_piece(projection(3,2, ghe, stakan5_10))