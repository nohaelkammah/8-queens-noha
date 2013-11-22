import random
from pprint import pprint
import numpy as np


finished = 0
#place queens

while finished == 0:
    board = [[0 for x in xrange(8)] for x in xrange(8)] #matrix
    for i in range (0,8,1):
        r = random.randrange(0,9)
        c = random.randrange(0,7)
        board[r][c]= 'Q'
        
    count = 0

    for c in range (0,8,1):
        for r in range (0,8,1):
            if board[r][c]== 'Q':
                count = count +1
    print count
    if count == 8:
        finished = 1
    else:
        continue
arr=np.array([board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7]])
print arr
