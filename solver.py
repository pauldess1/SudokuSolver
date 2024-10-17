from values import sudoku1

class SudokuSolver():
    
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.height = len(self.sudoku)
        self.width = len(self.sudoku[0])

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.is_valid(i, (row, col)):
                self.sudoku[row][col] = i

                if self.solve():
                    return True

                self.sudoku[row][col] = 0
        return False


    def is_valid(self, num, pos):
        # row
        for i in range(self.height):
            if self.sudoku[pos[0]][i] == num and pos[1] != i:
                return False

        # column
        for i in range(self.height):
            if self.sudoku[i][pos[1]] == num and pos[0] != i:
                return False

        # box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.sudoku[i][j] == num and (i,j) != pos:
                    return False
        return True


    def print_board(self):
        for i in range(self.height):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(self.height):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.sudoku[i][j])
                else:
                    print(str(self.sudoku[i][j]) + " ", end="")


    def find_empty(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.sudoku[i][j] == 0:
                    return (i, j)

        return None
    
    def resolve(self):
        self.print_board()
        self.solve()
        print("___________________")
        self.print_board()

# solver = SudokuSolver(sudoku1)
# solver.resolve()