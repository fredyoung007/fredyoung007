"""queens.py
Queens Problem
"""

def display():
    print(board)
    for r in range(n):
        row = ''
        for c in range(n):
            if board[r]==c:
                row += 'Q '
            else:
                row += '- '
        print(row)

# diagnol differnce in row equals diffirence in column
def attack(r,c):
    for i in range(r):
        if (board[i] == c) or (abs(board[i]-c)==abs(r-i)):
            return True
    return False
                
# for each row try each column from left to right for attack
def queen(r, n):
    global count
    for c in range(n):
        if not attack(r, c):
            board[r] = c
            if (r == n-1):
                count += 1
                print("Solution", count)
                display()
            else:
                queen(r+1, n)

n = 4
board = [0 for _ in range(n)]
count = 0
queen(0, n)




