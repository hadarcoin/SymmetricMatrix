import random


def finito():
    import sys
    print('this matrix is not what we searching for')
    sys.exit()


matrix = []

for i in range(4):
    print('\n')
    array_line = []
    for y in range(4):
        ran_num = random.randint(0, 9)
        array_line.append(ran_num)
    matrix.append(array_line)

matrix = [[1,2,3,4],[5,1,2,3],[4,5,1,2],[3,4,5,1]]
print(matrix)

count = 1
for y in range(4):
    for i in range(4):
        if (count == 4 or count == 8 or count == 12 or count == 13):
            count = count + 1
            break
        count = count + 1
        print(matrix[y][i])
        if (y == 3):
            next_line == y
        else:
            next_line = y+1
        if(i == 3):
            next_num == i
        else:
            next_num = i+1

        print(matrix[next_line][next_num])
        if (matrix[y][i] == matrix[next_line][next_num]):
            print('pass')
        else:
            finito()

