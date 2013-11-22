import random
import numpy

finished = 0
#place queens
boardn = numpy.zeros(shape=(8,8))

while finished == 0:
    col = [0,1,2,3,4,5,6,7]
    random.shuffle(col)

    board = [[0 for x in xrange(8)] for x in xrange(8)] #matrix
    for i in range (0,8,1):
        r = random.randrange(0,7)
        board[r][col[i]]= 'Q'
        
    count = 0 # count the queens in case there are repetitions

    for c in range (0,8,1):
        for r in range (0,8,1):
            if board[r][c]== 'Q':
                count = count +1
    if count == 8:
        finished = 1
    else:
        continue


print board

