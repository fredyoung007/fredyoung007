import math


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

    def clone(self):
        """Clone the board"""
        board = GameBoard(self.size)
        board.size = self.size
        board.num_entries = self.num_entries[:]
        board.items = [i[:] for i in self.items]
        board.points = self.points[:]
        return board

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

        # rotate item matrix 90 degress counter clockwise to render the board
        rotated = list(zip(*self.items))[::-1]
        for row in rotated:
            rs = ' '.join([str(_) for _ in row])
            print(rs.replace('0', ' ').replace('1', 'o').replace('2', 'x'))

        print('-' * (self.size * 2-1))
        print(' '.join(str(i) for i in range(self.size)))

        print("Points player 1: ", self.points[0])
        print("Points player 2: ", self.points[1])

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

        # Add horizontal points
        i = column
        count = 0
        while (i >= 0) and (self.items[i][row] == player):
            i -= 1
            count += 1

        i = column
        while (i < self.size) and (self.items[i][row] == player):
            i += 1
            count += 1
        if count > 4:
            points += 1
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row] == player) and (self.items[column+1][row] == player):
                    points += 1

        # Add vertical points
        i = row
        count = 0
        while (i >= 0) and (self.items[column][i] == player):
            i -= 1
            count += 1
        if count > 3:
            points += 1

        # Add diagonal points
        i = column
        j = row
        count = 0
        while (i >= 0) and (j < self.size) and (self.items[i][j] == player):
            i -= 1
            j += 1
            count += 1
        i = column
        j = row
        while (i < self.size) and (j >= 0) and (self.items[i][j] == player):
            i += 1
            j -= 1
            count += 1
        if count > 4:
            points += 1
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row+1] == player) and (self.items[column+1][row-1] == player):
                    points += 1

        # Add antidiagonal points
        i = column
        j = row
        count = 0
        while (i >= 0) and (j >= 0) and (self.items[i][j] == player):
            i -= 1
            j -= 1
            count += 1
        i = column
        j = row
        while (i < self.size) and (j < self.size) and (self.items[i][j] == player):
            i += 1
            j += 1
            count += 1
        if count > 4:
            points += 1
        if count > 5:
            # disk not at the end and both neighbours are the same disks
            if column != 0 and column != self.size-1:
                if (self.items[column-1][row-1] == player) and (self.items[column+1][row+1] == player):
                    points += 1

        return points

    def add(self, column, player):
        if (self.num_entries[column] >= self.size) or (column < 0) or (column >= self.size):
            return False

        row = self.num_entries[column]
        self.items[column][row] = player
        self.num_entries[column] = row + 1
        self.points[player-1] += self.num_new_points(column, row, player)
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
        sb = self.clone()

        for column in range(sb.size):
            sb.add(column, player)
            row = sb.num_entries[column]-1
            points.append(sb.num_new_points(column, row, player))
            sb = self.clone()            

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


class FourInARow:
    def __init__(self, size):
        self.board=GameBoard(size)
    def play(self):
        print("*****************NEW GAME*****************")
        self.board.display()
        player_number=0
        print()
        while not self.board.game_over():
            print("Player ",player_number+1,": ")
            if player_number==0:
                valid_input = False
                while not valid_input:
                    try:
                        column = int(input("Please input slot: "))       
                    except ValueError:
                        print("Input must be an integer in the range 0 to ", self.board.size)
                    else:
                        if column<0 or column>=self.board.size:
                            print("Input must be an integer in the range 0 to ", self.board.size)
                        else:
                            if self.board.add(column, player_number+1):
                                valid_input = True
                            else:
                                print("Column ", column, "is alrady full. Please choose another one.")
            else:
                # Choose move which maximises new points for computer player
                (best_column, max_points)=self.board.column_resulting_in_max_points(2)
                if max_points>0:
                    column=best_column
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (best_column, max_points)=self.board.column_resulting_in_max_points(1)
                    if max_points>0:
                        column=best_column
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]
                self.board.add(column, player_number+1)
                print("The AI chooses column ", column)
            self.board.display()   
            player_number=(player_number+1)%2
        if (self.board.points[0]>self.board.points[1]):
            print("Player 1 (circles) wins!")
        elif (self.board.points[0]<self.board.points[1]):    
            print("Player 2 (crosses) wins!")
        else:  
            print("It's a draw!")
            
game = FourInARow(6)
game.play()        
