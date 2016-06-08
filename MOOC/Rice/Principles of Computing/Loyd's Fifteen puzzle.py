"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if self.get_number(target_row, target_col) != 0:
            return False
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if col + self.get_width() * row != self.get_number(row, col):
                    return False
        
        for col in range(target_col + 1, self.get_width()):
            if col + self.get_width() * target_row != self.get_number(target_row, col):
                    return False      
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.get_height() > target_row > 1 and self.get_width() > target_col > 0, "wrong input"
        assert self.lower_row_invariant(target_row, target_col), "lower_row_invariant false"
        answer = ""
        current_row, current_col = self.current_position(target_row, target_col)
        diff_row = target_row - current_row
        diff_col = target_col - current_col
        if diff_col > 0 and diff_row > 0:
            answer += "u" * diff_row
            answer += "l" * (diff_col - 1)
            answer += "ldr"
            answer += "ruldr" * (diff_col - 1)
            answer += "u"
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        elif diff_col < 0 and diff_row > 0:
            answer += "u" * diff_row
            answer += "r" * (-diff_col - 1)
            if diff_row > 1:
                answer += "rdl"
            else:
                answer += "rullddr"
            answer += "ruldr" * (-diff_col - 1)
            answer += "u"
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        elif diff_row == 0:
            answer += "l" * diff_col
            answer += "urrdl" * (diff_col - 1)
        else:
            answer += "u" * diff_row
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        self.update_puzzle(answer)
        assert self.lower_row_invariant(target_row, target_col - 1), "solve_interior_tile mess up the tile"
        return answer

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        target_col = 0
        assert self.get_height() > target_row > 1, "wrong input"
        assert self.lower_row_invariant(target_row, target_col), "lower_row_invariant false"
        answer = ""
        current_row, current_col = self.current_position(target_row, target_col)
        diff_row = target_row - current_row
        diff_col = target_col - current_col
        if diff_row == 1 and diff_col == 0:
            self.update_puzzle("u" + "r" * (self.get_width() - 1))
            return "u" + "r" * (self.get_width() - 1)
        elif diff_row == 1 and diff_col == -1:
            self.update_puzzle("uruldrdlurdluurddlu" + "r" * (self.get_width() - 1))
            return "uruldrdlurdluurddlu" + "r" * (self.get_width() - 1)
        
        diff_row -= 1
        diff_col += 1
        answer += "ur"
        if diff_col > 0 and diff_row > 0:
            answer += "u" * diff_row
            answer += "l" * (diff_col - 1)
            answer += "ldr"
            answer += "ruldr" * (diff_col - 1)
            answer += "u"
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        elif diff_col < 0 and diff_row > 0:
            answer += "u" * diff_row
            answer += "r" * (-diff_col - 1)
            answer += "rdl"
            answer += "lurdl" * (-diff_col - 1)
            answer += "u"
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        elif diff_row == 0:
            answer += "r" * -diff_col
            answer += "ulldr" * (diff_col - 1)
            answer += "ulld"
        else:
            answer += "u" * diff_row
            answer += "lddru" * (diff_row - 1)
            answer += "ld"
        answer += "ruldrdlurdluurddlu" + "r" * (self.get_width() - 1)
        self.update_puzzle(answer)
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1), "solve_col0_tile mess up the tile"
        return answer

    #############################################################
    # Phase two methods
    
    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.get_number(1, target_col) != 0:
            return False
        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if col + self.get_width() * row != self.get_number(row, col):
                    return False
        for row in range(2):
            for col in range(target_col + 1, self.get_width()):
                if col + self.get_width() * row != self.get_number(row, col):
                    return False
        return True
    
    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.get_number(0, target_col) != 0:
            return False
        if target_col + self.get_width() != self.get_number(1, target_col):
            return False
        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if col + self.get_width() * row != self.get_number(row, col):
                    return False
        for row in range(2):
            for col in range(target_col + 1, self.get_width()):
                if col + self.get_width() * row != self.get_number(row, col):
                    return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col), "wrong used"
        assert target_col > 1, "wrong input"
        answer = ""
        current_row, current_col = self.current_position(0, target_col)
        diff_col = target_col - current_col
        diff_row = 0 - current_row
        if diff_col == 1 and diff_row == 0:
            self.update_puzzle("ld")
            return "ld"
        diff_col -= 1
        diff_row += 1
        answer += "ld"
        print "l" * (diff_col - 1) + "urrdl" * (diff_col - 1)
        if diff_col ==0: 
            answer += "uld"
        else:
            answer += "l" * (diff_col - 1) + "lurd" * diff_row
            answer += "l" + "urrdl" * (diff_col - 1)

        answer += "urdlurrdluldrruld"
        self.update_puzzle(answer)
        return answer

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col), "wrong used"
        assert target_col > 1, "wrong input"
        answer = ""
        current_row, current_col = self.current_position(1, target_col)
        diff_col = target_col - current_col
        diff_row = 1 - current_row
        if diff_col ==0: 
            self.update_puzzle("u")
            return "u"
        answer += "l" * (diff_col - 1) + "lurd" * diff_row
        answer += "l" + "urrdl" * (diff_col - 1)
        answer += "ur"
        self.update_puzzle(answer)
        assert self.row0_invariant(target_col), "solve_row1_tile mess up the tile"
        return answer

    ###########################################################
    # Phase 3 methods
    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1), "wrong used"
        answer = ""
        answer += "lu"
        self.update_puzzle("lu")
        for dummy_index in range(3):
            if self.row0_invariant(0):
                return answer
            else:
                answer += "rdlu"
                self.update_puzzle("rdlu")
        assert False,  "something wrong"


    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        answer = ""
        zero_row, zero_col = self.current_position(0, 0)
        answer += "r" * (self.get_width() - 1 - zero_col) +\
                  "d" * (self.get_height() - 1 - zero_row)
        self.update_puzzle(answer)
        for row in range(self.get_height() - 1, 1, -1):
            for col in range(self.get_width() - 1, -1, -1):
                if col > 0:
                    answer += self.solve_interior_tile(row, col)
                else:
                    answer += self.solve_col0_tile(row)
        for col in range(self.get_width() - 1, 1, -1):
            answer += self.solve_row1_tile(col)
            answer += self.solve_row0_tile(col)
        answer += self.solve_2x2()
        return answer

#test = Puzzle(4, 4, [[1, 5, 2, 3], [4, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
#print test
#print test.lower_row_invariant(0,0)
#test current position
#print test.current_position(1,1)
#print test.current_position(2,3)
#test update
#test.update_puzzle("ddd")
#print test
#print test.solve_interior_tile(2, 2)
#print test.solve_col0_tile(2)
#print test.row0_invariant()
#print test.row0_invariant() 
#print test.row1_invariant()
#print test.row1_invariant()
#print test.solve_2x2()
#obj = Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])
# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(obj)
#poc_fifteen_gui.FifteenGUI(test)

# for upmost urdlurrdluldrruld
# for leftmost ruldrdlurdluurddlu
