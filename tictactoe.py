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
        self.count_x = 0
        self.count_o = 0
        self.count_spaces = 0
        self.horizontal_cells = [[], [], []]
        self.vertical_cells = [[], [], []]
        self.diagonal_cells = [[], []]
        self.full_x_rows = 0
        self.full_o_rows = 0
        self.full_x_columns = 0
        self.full_o_columns = 0
        self.x_cross = 0
        self.o_cross = 0

    def print_grid(self, cells):
        k = 0
        for i in range(1, 4):
            for j in range(1, 4):
                if cells[k] == '_':
                    self.count_spaces += 1
                    self.grid[i][j] = '  '
                elif cells[k] == ('X' or 'x'):
                    self.count_x += 1
                    self.grid[i][j] = cells[k] + ' '
                else:
                    self.count_o += 1
                    self.grid[i][j] = cells[k] + ' '
                k += 1
        print(self.list_to_str())
        self.get_horizontal_cells(cells)
        self.get_vertical_cells(cells)
        self.get_diagonal_cells(cells)
        self.get_rows()
        self.get_columns()
        self.get_cross()

    def list_to_str(self):
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
        self.grid[line][column] = 'X' + ' '
        print(self.list_to_str())

    def get_horizontal_cells(self, cells):
        j = 0
        for i in range(3):
            for k in range(3):
                self.horizontal_cells[i].append(cells[k + j])
            j += 3

    def get_vertical_cells(self, cells):
        j = 0
        for i in range(3):
            for k in range(0, 9, 3):
                self.vertical_cells[i].append(cells[k + j])
            j += 1

    def get_diagonal_cells(self, cells):
        j = 0
        for k in range(0, 9, 4):
            self.diagonal_cells[0].append(cells[k + j])
        j += 2

        j = 0
        for k in range(2, 7, 2):
            self.diagonal_cells[1].append(cells[k + j])
        j += 2

    def get_state(self):
        # print(self.count_x, self.count_o)
        if (self.count_x - self.count_o) >= 2 or (self.count_o - self.count_x) >= 2:
            print('Impossible')
        else:
            if self.full_x_rows > 0 and self.full_o_rows > 0:
                print('Impossible')
            elif self.full_x_columns > 0 and self.full_o_columns > 0:
                print('Impossible')
            elif (self.full_x_rows == 1 or self.full_x_columns == 1 or self.x_cross == 1) \
                    and self.full_o_rows == 0 and self.full_o_columns == 0:
                print('X wins')
            elif (self.full_o_rows == 1 or self.full_o_columns == 1 or self.o_cross == 1) \
                    and self.full_x_rows == 0 and self.full_x_columns == 0:
                print('O wins')
            elif self.count_spaces == 0 \
                    and (self.full_x_rows == 0 or self.full_x_columns == 0) \
                    and (self.full_o_rows == 0 or self.full_o_columns == 0):
                print('Draw')
            elif self.count_spaces != 0 \
                    and (self.full_x_rows == 0 or self.full_x_columns == 0) \
                    and (self.full_o_rows == 0 or self.full_o_columns == 0):
                print('Game not finished')

    def get_rows(self):
        for i in range(len(self.horizontal_cells)):
            if self.horizontal_cells[i][0] == 'X' \
             and self.horizontal_cells[i][1] == 'X' \
             and self.horizontal_cells[i][2] == 'X':
                self.full_x_rows += 1

            if self.horizontal_cells[i][0] == 'O' \
             and self.horizontal_cells[i][1] == 'O' \
             and self.horizontal_cells[i][2] == 'O':
                self.full_o_rows += 1

    def get_columns(self):
        for i in range(len(self.vertical_cells)):
            if self.vertical_cells[i][0] == 'X' \
                    and self.vertical_cells[i][1] == 'X' \
                    and self.vertical_cells[i][2] == 'X':
                self.full_x_columns += 1

            if self.vertical_cells[i][0] == 'O' \
                    and self.vertical_cells[i][1] == 'O' \
                    and self.vertical_cells[i][2] == 'O':
                self.full_o_columns += 1

    def get_cross(self):
        for i in range(len(self.diagonal_cells)):
            if self.diagonal_cells[i][0] == 'X' \
                    and self.diagonal_cells[i][1] == 'X' \
                    and self.diagonal_cells[i][2] == 'X':
                self.x_cross += 1

            if self.diagonal_cells[i][0] == 'O' \
                    and self.diagonal_cells[i][1] == 'O' \
                    and self.diagonal_cells[i][2] == 'O':
                self.o_cross += 1


def main():
    game = TicTacToe()
    game.print_grid(input('Enter cells: '))
    while game.ask_input:
        user_coordinates = input('Enter the coordinates: ')
        if game.validate_coordinates(user_coordinates):
            game.update_grid(user_coordinates)
    # game.get_state()


main()
