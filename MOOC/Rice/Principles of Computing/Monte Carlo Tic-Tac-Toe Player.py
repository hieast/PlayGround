"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 30         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    '''
    board: type TTTBoard.
    player: constant PLAYERO or PLAYERX.
    return nothing, modify the board input.
    '''
    while board.check_win() == None:
        position = random.choice(board.get_empty_squares())
        board.move(position[0], position[1], player)
        player = provided.switch_player(player)
    
def mc_update_scores(scores, board, player):
    '''
    scores: a list of lists(a grid of scores) .
    board: type TTTBoard, the same dimension as scores.
    player: constant PLAYERO or PLAYERX.
    return nothing, updates the scores grid directly.
    '''
    if board.check_win() == provided.DRAW:
        return

    # (Winner, Square Owner):score
    update = {(player, player):SCORE_CURRENT, 
             (player, provided.switch_player(player)):-SCORE_OTHER, 
             (provided.switch_player(player), player):-SCORE_CURRENT, 
             (provided.switch_player(player), provided.switch_player(player)):SCORE_OTHER}
        
    dim = board.get_dim()
    for row in range(dim):
        for col in range(dim):
            if board.square(row, col) != provided.EMPTY:
                scores[row][col] += update[(board.check_win(), board.square(row, col))]

    print board
    print scores
    
def get_best_move(board, scores):
    '''
    board: type TTTBoard, the same dimension as scores.
    scores: a list of lists(a grid of scores) .
    return a tuple, one of the maximum score as (row, column) .
    '''
    
    empty_squares = board.get_empty_squares()
    if empty_squares == []:
        raise ValueError
    max_pos = random.choice(empty_squares)
    max_score = scores[max_pos[0]][max_pos[1]]
    
    for pos in empty_squares:
        if scores[pos[0]][pos[1]] > max_score:
            max_score = scores[pos[0]][pos[1]]
            max_pos = pos
    return max_pos

def mc_move(board, player, trials):
    '''
    board: type TTTBoard, the same dimension as scores.
    player: constant PLAYERO or PLAYERX.
    trials: positive int, number of trials to run.
    Return a move for the machine player (row, column).
    '''
    dim = board.get_dim()
    scores = [[0 for dummy_i in range(dim)] for dummy_j in range(dim)]
    for dummy_trial in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores, clone_board, player)
    move = get_best_move(board, scores)
    return move

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
