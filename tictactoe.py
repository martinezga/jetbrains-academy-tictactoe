class TicTacToe:
    def __init__(self):
        self.ask_input = True
        self.grid = [
                     ['--', '--', '--', '--', '-'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n--', '--', '--', '--', '-'],
                    ]
        print(self.grid_str())
        self.player = 'X'
        self.count_x = 0
        self.count_o = 0
        self.count_spaces = 9
        self.horizontal_cells = [['', '', ''], ['', '', ''], ['', '', '']]
        self.vertical_cells = [['', '', ''], ['', '', ''], ['', '', '']]
        self.diagonal_cells = [['', '', ''], ['', '', '']]
        self.full_x_rows = 0
        self.full_o_rows = 0
        self.full_x_columns = 0
        self.full_o_columns = 0
        self.x_cross = 0
        self.o_cross = 0

    def grid_str(self):
        str_grid = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                str_grid += self.grid[i][j]
        return str_grid

    def validate_coordinates(self, coordinates):
        if (coordinates[0].isnumeric() is False) or (coordinates[2].isnumeric() is False):
            print('You should enter numbers!')
            return False
        elif (int(coordinates[0]) < 1 or int(coordinates[0]) > 3) \
                or (int(coordinates[2]) < 1 or int(coordinates[2]) > 3):
            print('Coordinates should be from 1 to 3!')
            return False
        elif self.grid[int(coordinates[0])][int(coordinates[2])] != '  ':
            print('This cell is occupied! Choose another one!')
            return False
        self.ask_input = False
        return True

    def update_grid(self, coordinates):
        line = int(coordinates[0])
        column = int(coordinates[2])
        self.grid[line][column] = self.player + ' '
        print(self.grid_str())
        self.count_moves()
        self.change_player()
        self.get_horizontal_cells()
        self.get_vertical_cells()
        self.get_diagonal_cells()
        self.get_rows()
        self.get_columns()
        self.get_cross()

    def count_moves(self):
        if self.player == 'X':
            self.count_x += 1
        else:
            self.count_o += 1
        self.count_spaces -= 1

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def get_horizontal_cells(self):
        horizontal_column = 0
        grid_line = 1
        for line in range(3):
            for grid_column in range(1, 4):
                self.horizontal_cells[line][horizontal_column] = self.grid[grid_line][grid_column]
                horizontal_column += 1
            horizontal_column = 0
            grid_line += 1

    def get_vertical_cells(self):
        vertical_column = 0
        grid_column = 1
        for line in range(3):
            for grid_line in range(1, 4):
                self.vertical_cells[line][vertical_column] = self.grid[grid_line][grid_column]
                vertical_column += 1
            vertical_column = 0
            grid_column += 1

    def get_diagonal_cells(self):
        # To get grid cells (1,1) (2,2) (3,3)
        diagonal_index = 0
        for grid_index in range(1, 4):
            self.diagonal_cells[0][diagonal_index] = self.grid[grid_index][grid_index]
            diagonal_index += 1

        # To get grid cells (1,3) (2,2) (3,1)
        diagonal_index = 0
        j = 3
        for grid_index in range(1, 4):
            self.diagonal_cells[1][diagonal_index] = self.grid[grid_index][j]
            j -= 1
            diagonal_index += 1

    def get_state(self):
        if (self.count_x - self.count_o) >= 2 or (self.count_o - self.count_x) >= 2:
            print('Impossible')
            return True
        else:
            if self.full_x_rows > 0 and self.full_o_rows > 0:
                print('Impossible')
                return True
            elif self.full_x_columns > 0 and self.full_o_columns > 0:
                print('Impossible')
                return True
            elif (self.full_x_rows == 1 or self.full_x_columns == 1 or self.x_cross == 1) \
                    and self.full_o_rows == 0 and self.full_o_columns == 0:
                print('X wins')
                return False
            elif (self.full_o_rows == 1 or self.full_o_columns == 1 or self.o_cross == 1) \
                    and self.full_x_rows == 0 and self.full_x_columns == 0:
                print('O wins')
                return False
            elif self.count_spaces == 0 \
                    and (self.full_x_rows == 0 or self.full_x_columns == 0) \
                    and (self.full_o_rows == 0 or self.full_o_columns == 0):
                print('Draw')
                return False
            elif self.count_spaces != 0 \
                    and (self.full_x_rows == 0 or self.full_x_columns == 0) \
                    and (self.full_o_rows == 0 or self.full_o_columns == 0):
                # print('Game not finished')
                return True

    def get_rows(self):
        for i in range(len(self.horizontal_cells)):
            if self.horizontal_cells[i][0] == 'X ' \
             and self.horizontal_cells[i][1] == 'X ' \
             and self.horizontal_cells[i][2] == 'X ':
                self.full_x_rows += 1

            if self.horizontal_cells[i][0] == 'O ' \
             and self.horizontal_cells[i][1] == 'O ' \
             and self.horizontal_cells[i][2] == 'O ':
                self.full_o_rows += 1

    def get_columns(self):
        for i in range(len(self.vertical_cells)):
            if self.vertical_cells[i][0] == 'X ' \
                    and self.vertical_cells[i][1] == 'X ' \
                    and self.vertical_cells[i][2] == 'X ':
                self.full_x_columns += 1

            if self.vertical_cells[i][0] == 'O ' \
                    and self.vertical_cells[i][1] == 'O ' \
                    and self.vertical_cells[i][2] == 'O ':
                self.full_o_columns += 1

    def get_cross(self):
        for i in range(len(self.diagonal_cells)):
            if self.diagonal_cells[i][0] == 'X ' \
                    and self.diagonal_cells[i][1] == 'X ' \
                    and self.diagonal_cells[i][2] == 'X ':
                self.x_cross += 1

            if self.diagonal_cells[i][0] == 'O ' \
                    and self.diagonal_cells[i][1] == 'O ' \
                    and self.diagonal_cells[i][2] == 'O ':
                self.o_cross += 1


def main():
    game = TicTacToe()
    while game.get_state():
        user_coordinates = input('Enter the coordinates: ')
        if game.validate_coordinates(user_coordinates):
            game.update_grid(user_coordinates)


main()
