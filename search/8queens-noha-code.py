import random
import numpy as np

def makeboard():
    finished = 0
    #place queens

    while finished == 0:
        col = [0,1,2,3,4,5,6,7]
        random.shuffle(col)

        board = [[0 for x in xrange(8)] for x in xrange(8)] #matrix
        for i in range (0,8,1):
            r = random.randrange(0,8)
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
    return board

board = makeboard()


boardn = np.array([board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7]])
print boardn


#hill climbing
loc = []
c = 0

while c != 8:

    for r in range (0,8,1):
        if board[r][c]== 'Q':
            loc = [r,c]

    rown = loc[0]
    cp1 = c+1
    cm1 = c-1
    for r in range(0,8,1):
        if c == 0:
            if board[r][cp1] == 'Q':
                if r == rown:
                    print 'oppa collision yemeen of queen in column',c
                elif r == rown+1:
                    print 'oppa collision diag ta7t yemeen of queen in column',c
                elif r == rown-1:
                    print 'oppa collision diag fo2 yemeen of queen in column',c
        
        elif c ==7:
            if board[r][cm1] == 'Q':
                if r == rown:
                    print 'oppa collision shemal of queen in column',c
                elif r == rown+1:
                    print 'oppa collision diag ta7t shemal of queen in column',c
                elif r == rown-1:
                    print 'oppa collision diag fo2 shemal of queen in column',c
                    
        elif c>0 or c<7:
            if board[r][cm1] == 'Q':
                if r == rown:
                    print 'oppa collision shemal of queen in column',c
                elif r == rown+1:
                    print 'oppa collision diag ta7t shemal of queen in column',c
                elif r == rown-1:
                    print 'oppa collision diag fo2 shemal of queen in column',c
            elif board[r][cp1] == 'Q': 
                if r == rown:
                    print 'oppa collision yemeen of queen in column',c
                elif r == rown+1:
                    print 'oppa collision diag ta7t yemeen of queen in column',c
                elif r == rown-1:
                    print 'oppa collision diag fo2 yemeen of queen in column',c
                
            
    c = c+1 
