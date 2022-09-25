"""queens.py
Queens Problem
DFS backtracking
Time O(n^2) Space O(n)
"""

def display():
    for bd in solutions:
        bd = [['Q' if board[r]==c else '-' for r in range(n)] for c in range(n)]
        for row in bd:
            print(' '.join(row))
    print("Totaly found {0} solutions for {1} queens problem.".format(len(solutions), n))

# same row/column or diagnol (differnce in row equals diffirence in column)
def attack(r,c):
    for i in range(r):
        if (board[i] == c) or (abs(board[i]-c)==abs(r-i)):
            return True
    return False

# depth first top down for each row, then left to right for each column
def queen(r, n):
    global solutions
    if (r==n):
        solutions.append(board)

    for c in range(n): # backtrack left to right
        if not attack(r, c):
            board[r] = c
            queen(r+1, n) # depth first

n = 8
board = [0 for _ in range(n)]
solutions = []

queen(0, n)
display()




