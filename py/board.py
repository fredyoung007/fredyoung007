class GameBoard:
    def __init__(self, size):
        self.size=size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] *2
        
    
    def num_free_positions_in_column(self, column):
        space = self.size - self.num_entries[column]
        return space

    def game_over(self):
        for column in range (0, self.size + 1):
            if GameBoard.num_free_positions_in_column(self, column) == 0:
                return True
            return False

    def display(self):
        rotated = list(zip(*self.items))[::-1]
        for row in rotated:
            rs = ' '.join([str(_) for _ in row])
            print(rs.replace('0', ' ').replace('1', 'o').replace('2','x'))
            
        print('-' * (self.size * 2-1))
        print(' '.join(str(i) for i in range(self.size)))

        print("Points player 1: ", self.points[0])
        print("Points player 2: ", self.points[1])

board = GameBoard(4)
board.items[2][0]=1
board.items[2][1]=2
board.num_entries[2]=2
print("Num free items in column 1:",board.num_free_positions_in_column(1))
print("Num free items in column 2:",board.num_free_positions_in_column(2))
print("Game is over:",board.game_over())
board.display()
print("")

board = GameBoard(2)
board.items[0][0]=1
board.items[0][1]=2
board.items[1][0]=1
board.items[1][1]=2
board.display()