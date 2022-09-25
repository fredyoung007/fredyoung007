##
#
# A variation of Connect Four game
# with following addtional cool features:
# 
# 1. reset board
# 2. undo moves
# 3. dispaly existng 4-in-a-row sequences on the board in Capital letters
# 4. GUI game display, with 4-in-a-row sequences highlighted
#
##

import math
import copy
from tkinter import *
from tkinter import ttk
from tkinter import font


class GameBoard:
    """class GameBoard:
    A variation of Connect Four game, where:
    - board is square nxn grid of n rows and n columns
    - columns (slots) left to right from 0 to n-1
    - rows are bottom up from 0 to n-1
    - disk tuple (i, j) is disck in column i, row j
    - 2 players:
        -- player 1 value is 1 and disk is 'o'
        -- player 2 value is 2 and disk is 'x'
    - pieces are connected horizontally, vertically and diagnally
    - if connected pieces > 4, then it counts as line of 4 connected pieces
    - when board is full with nxn disks, player with more lines of 4 connected pieces wins
    """

    def __init__(self, size):
        """Board constructor"""
        self.size = size  # size of the board
        self.num_entries = [0] * size   # number of disks in each column
        self.items = [[0] * size for i in range(size)]  # the board of (column, row)
        self.points = [0] * 2    # points for player 1, 2
        self.moves = [] # moves played so far
        self.sequences = [] # 4-in-a-row sequences on the board

    def num_free_positions_in_column(self, column):
        """Returns the number of free positions in column column"""
        space = self.size - self.num_entries[column]
        return space

    def game_over(self):
        """A game is over if none of the columns has any free positions.
        returns:
            bool: True if the game is over and otherwise Fals
        """
        # return all(_==self.size for _ in self.num_entries)
        for column in range(0, self.size):
            if self.num_free_positions_in_column(column) != 0:
                return False
            return True

    def display(self):
        """Display board columns left to right from 0 to n-1, rows bottom top from 0 to n-1"""

        sequences = set(sum(self.sequences, []))
        # rotate item matrix 90 degress counter clockwise to render the board
        rotated = list(zip(*self.items))[::-1]

        for i in range(self.size):
            rs = []
            for j in range(self.size):
                if rotated[i][j] == 0:
                    rs.append(' ')
                if rotated[i][j] == 1:
                    if (j, self.size-i-1) in sequences:
                        rs.append('O')
                    else:
                        rs.append('o')
                if rotated[i][j] == 2:
                    if (j, self.size-i-1) in sequences:
                        rs.append('X')
                    else:
                        rs.append('x')
            print(' '.join(rs))
  
        print('-' * (self.size * 2-1))
        print(' '.join(str(i) for i in range(self.size)))

        print("Points player 1: ", self.points[0])
        print("Points player 2: ", self.points[1])

        # print("Moves played: ", self.moves)
        # print("4-in-a-row sequences on the board: ", self.sequences)

    def num_new_points(self, column, row, player):
        """Calculates how many 4-in-a-row sequences a newly inserted disk creates
        args:
            column: int, inserted disk column position
            row: int, inserted disk row position
            player: which player inserts the disk
        returns:
            int: number of 4-in-a-row sequences newly createdy as points
        """

        points = 0
        sequence = []
        sequences = []

        # Add horizontal points
        i = column
        count = 0
        while (i >= 0) and (self.items[i][row] == player):
            sequence.append((i, row))
            i -= 1
            count += 1

        i = column
        while (i < self.size) and (self.items[i][row] == player):
            sequence.append((i, row))
            i += 1
            count += 1
        if count > 4:
            points += 1
            sequences.append(sorted(list(set(sequence))))
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row] == player) and (self.items[column+1][row] == player):
                    points += 1

        # Add vertical points
        i = row
        count = 0
        sequence = []
        while (i >= 0) and (self.items[column][i] == player):
            sequence.append((column, i))
            i -= 1
            count += 1
        if count > 3:
            points += 1
            sequences.append(sorted(list(set(sequence))))

        # Add diagonal points
        i = column
        j = row
        count = 0
        sequence = []
        while (i >= 0) and (j < self.size) and (self.items[i][j] == player):
            sequence.append((i, j))
            i -= 1
            j += 1
            count += 1
        i = column
        j = row
        while (i < self.size) and (j >= 0) and (self.items[i][j] == player):
            sequence.append((i, j))
            i += 1
            j -= 1
            count += 1
        if count > 4:
            points += 1
            sequences.append(sorted(list(set(sequence))))
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row+1] == player) and (self.items[column+1][row-1] == player):
                    points += 1

        # Add antidiagonal points
        i = column
        j = row
        count = 0
        sequence = []
        while (i >= 0) and (j >= 0) and (self.items[i][j] == player):
            sequence.append((i, j))
            i -= 1
            j -= 1
            count += 1
        i = column
        j = row
        while (i < self.size) and (j < self.size) and (self.items[i][j] == player):
            sequence.append((i, j))            
            i += 1
            j += 1
            count += 1
        if count > 4:
            points += 1
            sequences.append(sorted(list(set(sequence))))
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row-1] == player) and (self.items[column+1][row+1] == player):
                    points += 1

        if points > 0:
            self.sequences += sequences
        return points

    def add(self, column, player):
        if (self.num_entries[column] >= self.size) or (column < 0) or (column >= self.size):
            return False

        row = self.num_entries[column]
        self.items[column][row] = player
        self.num_entries[column] = row + 1
        self.points[player-1] += self.num_new_points(column, row, player)
        self.moves.append((column, player))
        return True

    def free_slots_as_close_to_middle_as_possible(self):
        slots = []
        if self.size == 1:
            return [0]

        m = math.floor((self.size-1)/2)
        i = m
        if (self.size % 2 == 1):
            if (self.num_entries[m] < self.size):
                slots.append(m)
            i = m-1

        j = m + 1
        while True:
            if (self.num_entries[i] < self.size):
                slots.append(i)
            if (self.num_entries[j] < self.size):
                slots.append(j)
            i -= 1
            j += 1
            if (i < 0) or (j > self.size-1):
                break

        return slots

    def column_resulting_in_max_points(self, player):
        points = []

        # make a deep copy of the board for addition of disks on each slots
        # such that origianl board not changed by this function
        sb = copy.deepcopy(self)

        for column in range(sb.size):
            sb.add(column, player)
            row = sb.num_entries[column]-1
            points.append(sb.num_new_points(column, row, player))
            sb = copy.deepcopy(self)                  

        mx = max(points)    # maximum points

        # list of maximum point tuples
        mxindices = [i for i, x in enumerate(points) if x == mx]

        if len(mxindices) == 1:
            return (mxindices[0], mx)   # max point tutple(index, max point)

        # If multiple maximum point slots exist,
        # the closest slot to the middle of the board is returned,
        # using method free_slots_as_close_to_middle_as_possible()
        for i in sb.free_slots_as_close_to_middle_as_possible():
            if i in mxindices:
                return (i, mx)

    def reset_board(self):
        """Reset board to initial state"""
        self.__init__(self.size)    # clear the board


    def undo_moves(self, n):
        """undo the last n moves"""

        moves = copy.deepcopy(self.moves)
        for i in range(n):
            moves.pop()

        self.reset_board()    # clear the board
        for m in moves:
            self.add(m[0], m[1])

    def cool_display(self):
        """Display board with GUI"""
        root = Tk()
        root.title("Connect Four")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        cells = {}
        sequences = set(sum(self.sequences, []))
        # rotate item matrix 90 degress counter clockwise to render the board
        rotated = list(zip(*self.items))[::-1]
        
        for i in range(self.size):
            root.rowconfigure(i, weight=1, minsize=60)
            root.columnconfigure(i, weight=1, minsize=60)
            for j in range(self.size):
                if rotated[i][j] == 0:
                    disk = ('', 'black', 'lightblue')
                if rotated[i][j] == 1:
                    if (j, self.size-i-1) in sequences:
                        disk = ('O', 'red', 'yellow')
                    else:
                        disk = ('o', 'red', 'lightblue')
                if rotated[i][j] == 2:
                    if (j, self.size-i-1) in sequences:
                        disk = ('X', 'black', 'yellow')
                    else:
                        disk = ('x', 'black',  'lightblue')

                button = Button(
                    master = frm,
                    width = 3,
                    height = 2,
                    text = disk[0],                   
                    font = font.Font(size=38, weight="bold"),
                    fg = disk[1],
                    highlightbackground = disk[2]
                )
                cells[button] = (i, j)
                button.grid(
                    row=i,
                    column=j,
                )        
        
        frm.pack()
        root.mainloop()

board = GameBoard(5)
board.add(0,1)
board.add(0,2)
board.add(1,1)
board.add(1,2)
board.add(2,1)
board.add(0,2)
board.add(2,1)
board.add(2,2)
board.add(1,1)
board.add(1,2)
board.add(0,1)
board.add(0,2)
board.add(3,1)
board.display()
board.cool_display()

board = GameBoard(5)
board.add(0,1)
board.add(0,2)
board.add(0,2)
board.add(0,2)
board.add(1,1)
board.add(2,1)
board.add(2,2)
board.add(2,1)
board.add(3,1)
board.add(3,2)
board.add(3,2)
board.add(3,1)
board.add(4,1)
board.add(4,2)
board.add(1,1)
board.display()
board.cool_display()
board.undo_moves(2)
board.display()
board.add(1,2)
board.display()
board.cool_display()
board.reset_board()
board.display()


