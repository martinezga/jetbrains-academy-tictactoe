class TicTacToe:
    def __init__(self):
        self.grid = [
                     ['--', '--', '--', '--', '-'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n| ', '  ', '  ', '  ', '|'],
                     ['\n--', '--', '--', '--', '-'],
                    ]

    def print_grid(self, cells):
        k = 0
        for i in range(1, 4):
            for j in range(1, 4):
                self.grid[i][j] = cells[k] + ' '
                k += 1
        list_to_str = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                list_to_str += self.grid[i][j]
        print(list_to_str)


def main():
    game = TicTacToe()
    game.print_grid(input('Enter cells: '))


main()
