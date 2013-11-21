import random



finished = 0
#place queens

while finished == 0:
    board = [[0 for x in xrange(8)] for x in xrange(8)] #matrix
    for i in range (0,8,1):
        r = random.randrange(0,7)
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
        print "still goin"
        continue

print board
