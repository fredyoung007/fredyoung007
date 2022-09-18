"""8q.py
8 Queens Problem
"""

N = 8
queens = [0 for _ in range(N)]
board = [[0]*8 for _ in range(N)]

# diagnol differnce in row equals diffirence in column
def attack(i,j):
    # return (queens[i] == j) or (queens[i]==j+r-i) or (queens[i]==j-r+i)
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True

    for k in range(0,N):
        for l in range(0,N):
            if (abs(k-i)==abs(j-l)) and (board[k][l])==1:
                return True
    return False

                
# for each row try each column for attack, top down, left to right
def nQueens(n):
    if (n==0):
        return True

    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if nQueens(n-1):
                    return True
                board[i][j] = 0

    return False

nQueens(8)
for i in board:
    print(i)