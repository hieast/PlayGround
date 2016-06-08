"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    lengh = len(line)
    res = []
    skip = False
    for idx in range(lengh):
        if line[idx]:
            if skip:
                res.append(line[idx])
                skip = not skip
            else:
                if res == [] or res[-1] != line[idx]:
                    res.append(line[idx])
                else:
                    res[-1] *= 2
                    skip = True

    res = res + [0] * (lengh - len(res))
    return res

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        
        # initial tiles indices for different directions
        self._indices = {}
        help_dir = {UP:((0, 0), grid_height, grid_width, (0, 1)), 
                DOWN:((grid_height - 1, 0), grid_height, grid_width, (0, 1)), 
                LEFT:((0, 0), grid_width, grid_height, (1, 0)), 
                RIGHT:((0, grid_width - 1), grid_width, grid_height, (1, 0))}
        for direction in help_dir:
            self._indices[direction] = []
            for list_index in range(help_dir[direction][2]):
                self._indices[direction].append([])
                for step in range(help_dir[direction][1]):
                    row = help_dir[direction][0][0] + step * OFFSETS[direction][0] + list_index * help_dir[direction][3][0]
                    col = help_dir[direction][0][1] + step * OFFSETS[direction][1] + list_index * help_dir[direction][3][1]
                    self._indices[direction][list_index].append((row, col))

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = []
        for row in range(self._grid_height):
            self._grid.append([])
            for col in range(self._grid_width):
                self._grid[row].append(0)
        self.new_tile()
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    self.new_tile()
                    return

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        res = "["
        for row in self._grid:
            res += str(row) + "\n "
        res = res[:-2] + "]"
        return res

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def get_indices(self):
        """
        Get the indices of the grid
        """
        res = ""
        for direction in self._indices:
            res += str(direction) + ":\n"
            for indices in self._indices[direction]:
                res += str(indices) + "\n"
        return res
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        genetate = False
        for line in self._indices[direction]:
            before = []
            for index in line:
                before.append(self._grid[index[0]][index[1]])
            after = merge(before)
            for idx in range(len(after)):
                if after[idx] != before[idx]:
                    genetate = True
            for index in line:
                self._grid[index[0]][index[1]] = after.pop(0)
        if not genetate:
            return
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    self.new_tile()
                    return 

    def new_tile(self, probability = 0.9):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randrange(self._grid_height)
        col = random.randrange(self._grid_width)
        while self._grid[row][col] != 0:
            row = random.randrange(self._grid_height)
            col = random.randrange(self._grid_width)
        if random.random() <= 0.9:
            self._grid[row][col] = 2
        else:
            self._grid[row][col] = 4
            

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

#print TwentyFortyEight(1, 1)
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
