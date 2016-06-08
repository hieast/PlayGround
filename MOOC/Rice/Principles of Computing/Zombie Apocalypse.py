"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

#import codeskulptor
#codeskulptor.set_timeout(20)


# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """ 
        for dummy_row in range(self._grid_height):
            for dummy_col in range(self._grid_width):
                self._cells[dummy_row][dummy_col] = EMPTY
        self._zombie_list = []
        self._human_list = []
        
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list) 
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
        # claim local variables
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [[EMPTY for dummy_col in range(self._grid_width)] 
                           for dummy_row in range(self._grid_height)]
        boundary = poc_queue.Queue()
        entitys = []
        
        # initialize visited and distance_field
        for dummy_row in range(self._grid_height):
            for dummy_col in range(self._grid_width):
                if not self.is_empty(dummy_row, dummy_col):
                    visited.set_full(dummy_row, dummy_col)
                    distance_field[dummy_row][dummy_col] = self._grid_height * self._grid_width

        if entity_type == HUMAN:
            entitys = self._human_list
        elif entity_type == ZOMBIE:
            entitys = self._zombie_list
        
        for entity in entitys:
            boundary.enqueue(entity)
            visited.set_full(entity[0], entity[1])
            distance_field[entity[0]][entity[1]] = 0
        while(len(boundary)):
            cell = boundary.dequeue()
            neighbors = visited.four_neighbors(cell[0], cell[1])
            #neighbors = visited.eight_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
        for dummy_row in range(self._grid_height):
            for dummy_col in range(self._grid_width):
                if visited.is_empty(dummy_row, dummy_col):
                    visited.set_full(dummy_row, dummy_col)
                    distance_field[dummy_row][dummy_col] = self._grid_height * self._grid_width
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        human_result = []
        for human in self.humans():
            neighbors = self.eight_neighbors(human[0], human[1])
            maximal_distance = zombie_distance_field[human[0]][human[1]]
            maximal_neighbor = [human]
            for neighbor in neighbors:
                if not self.is_empty(neighbor[0], neighbor[1]):
                    continue
                if zombie_distance_field[neighbor[0]][neighbor[1]] > maximal_distance:
                    maximal_neighbor = [neighbor]
                    maximal_distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                elif zombie_distance_field[neighbor[0]][neighbor[1]] == maximal_distance:
                    maximal_neighbor.append(neighbor)
            human_result.append(random.choice(maximal_neighbor))
        self._human_list = human_result
            
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        zombie_result = []
        for zombie in self.zombies():
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            minimal_distance = human_distance_field[zombie[0]][zombie[1]]
            minimal_neighbor = [zombie]
            for neighbor in neighbors:
                if not self.is_empty(neighbor[0], neighbor[1]):
                    continue
                if human_distance_field[neighbor[0]][neighbor[1]] < minimal_distance:
                    minimal_neighbor = [neighbor]
                    minimal_distance = human_distance_field[neighbor[0]][neighbor[1]]
                elif human_distance_field[neighbor[0]][neighbor[1]] == minimal_distance:
                    minimal_neighbor.append(neighbor)
            zombie_result.append(random.choice(minimal_neighbor))
        self._zombie_list = zombie_result
    
    def print_map(self):
        """
        just print
        """
        for row in self._cells:
            for cell in row:
                if cell:
                    print 1,
                else:
                    print 0,
            print "\n"
        print "\n"

    

#game = Apocalypse(4, 4, [(0,0), (1,1)], [(0,1)], [(2,2)])
#game.print_map()
#
#boundary = poc_queue.Queue()
#print boundary
#print len(boundary) == 0
#
#print game.num_zombies()
#for zombie in game.zombies():
#    print zombie
#game.add_zombie(1,0)
#print game.num_zombies()
#for zombie in game.zombies():
#    print zombie
#
#print game.num_humans()    
#for human in game.humans():
#    print human
#game.add_human(2,3)
#print game.num_humans()
#for human in game.humans():
#    print human
#
#for line in game.compute_distance_field(ZOMBIE):
#    print line


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))
