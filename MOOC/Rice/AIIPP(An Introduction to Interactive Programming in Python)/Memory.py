# implementation of card game - Memory

import simplegui
import random

numList = [i % 8 for i in range(16)]
isVisi = [False for i in range(16)]
turns = 0
temp = []
color = {False:"Green", True:"Black"}
win = False


# helper function to initialize globals
def new_game():
    global numList, isVisi, turns, temp1, temp2, win
    turns = 0
    temp = []
    win = False
    random.shuffle(numList)
    isVisi = [False for i in range(16)]
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global temp, turns, win
    # test if you win the game and whether this card exposed
    i = pos[0] // 50
    if sum(isVisi) == 16:
        win = True
        return None
    elif isVisi[i]:
        return None
    else:
        if len(temp)==2:
            if numList[temp[0]] != numList[temp[1]]:
                isVisi[temp[0]] = not isVisi[temp[0]]
                isVisi[temp[1]] = not isVisi[temp[1]]
                temp = []
            else:
                temp = []
        elif len(temp)==1:
            turns += 1
            label.set_text("Turns = " + str(turns))
                
        isVisi[i] = not isVisi[i]
        temp.append(i)
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    if win == True:
        canvas.draw_text("You Win! Turns = " + str(turns), [5, 80], 80, "White")
        return None
    
    for i in range(16):
        canvas.draw_polygon([(50 * i, 0), (50 * i, 100), 
                            (50 * (i + 1), 100), (50 * (i + 1), 0)], 
                            3, "White", color[isVisi[i]])
        if isVisi[i]:
            canvas.draw_text(str(numList[i]), [5 + 50 * i , 80], 80, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric