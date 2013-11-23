import random
import numpy as np
import threading
import thread

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
    boardn = np.array([board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7]])
    return boardn,board



def fixallcollisions(boardn,board):
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
                if boardn[r][cp1] == 'Q':
                    if r == rown:
                        print 'oppa collision yemeen of queen in column',c
                        boardn[:,1]=np.roll(boardn[:,1], 2)
                    elif r == rown+1:
                        boardn[:,1]=np.roll(boardn[:,1], 1)
                        print 'oppa collision diag ta7t yemeen of queen in column',c
                    elif r == rown-1:
                        print 'oppa collision diag fo2 yemeen of queen in column',c
                        boardn[:,1]=np.roll(boardn[:,1], -1)

            elif c ==7:
                if boardn[r][cm1] == 'Q':
                    if r == rown:
                        print 'oppa collision shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], 2)

                    elif r == rown+1:
                        print 'oppa collision diag ta7t shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], 1)

                    elif r == rown-1:
                        print 'oppa collision diag fo2 shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], -1)

            elif c>0 or c<7:
                if boardn[r][cm1] == 'Q':
                    if r == rown:
                        print 'oppa collision shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], 2)

                    elif r == rown+1:
                        print 'oppa collision diag ta7t shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], 1)
                        
                    elif r == rown-1:
                        print 'oppa collision diag fo2 shemal of queen in column',c
                        boardn[:,cm1]=np.roll(boardn[:,cm1], -1)

                    
                elif boardn[r][cp1] == 'Q':
                    if r == rown:
                        print 'oppa collision yemeen of queen in column',c
                        boardn[:,cp1]=np.roll(boardn[:,cp1], 2)

                    elif r == rown+1:
                        print 'oppa collision diag ta7t yemeen of queen in column',c
                        boardn[:,cp1]=np.roll(boardn[:,cp1], 1)

                    elif r == rown-1:
                        print 'oppa collision diag fo2 yemeen of queen in column',c
                        boardn[:,cp1]=np.roll(boardn[:,cp1], -1)
        c = c+1
    return boardn


def getH(boardn):
    h = 0
    c = 0
    loc = []
    while c != 8:
        for r in range (0,8,1): #find a queen per column
            if boardn[r][c]== 'Q':
                loc = [r,c]
                
        begin = loc[1]+1
        for col in range(begin,8,1): # look horizontally to the right
            if boardn[loc[0]][col] == 'Q':
                h = h+1

        xr = loc[0]+1
        yc = loc[1]+1

        while xr< 8 and yc < 8: # look diagonally down
            if boardn[xr][yc] =='Q':
                h = h+1
                xr = xr+1
                yc = yc+1
            else:
                xr = xr+1
                yc = yc+1

        xr = loc[0]+1
        yc = loc[1]+1
        while xr >= 0 and yc < 8 and xr<8:# look diagonally up
            if boardn[xr][yc] =='Q':
                h = h+1
                xr = xr-1
                yc = yc+1
            else:
                xr = xr-1
                yc = yc+1
        c = c+1
    return h



def annealing(times):
    while times!= 0:
        boardn,board = makeboard()
        print boardn
        boardn = fixallcollisions(boardn,board)
        print "after:"
        print boardn
        h = 0
        h = getH(boardn)
        print 'heuristic = ',h
        times = times -1

times = 10
annealing(times)
