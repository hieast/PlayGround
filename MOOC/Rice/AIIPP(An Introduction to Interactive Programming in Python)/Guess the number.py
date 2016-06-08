# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

guess = None
secret_number = None
remain_guesses = None
total_guesses = 7
choice = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global remain_guesses
    secret_number = random.randrange(0,choice)
    remain_guesses = total_guesses
    print "New game. Range is [0," + str (choice) + ")"
    print "Number of remaining guesses is " + str(remain_guesses) + "\n"
    


# define event handlers for control panel
def range100():
    global total_guesses
    global choice
    total_guesses = 7
    choice = 100
    new_game()

def range1000():
    global total_guesses
    global choice
    total_guesses = 10
    choice = 1000
    new_game()
    
def input_guess(text):
    """
    convert guess from a string to an integer
    print out messages
    """
    
    global remain_guesses
    global guess
    guess = int(text)
    remain_guesses -= 1
    
    print "Guess was " + text
    print "Number of remaining guesses is " + str(remain_guesses)

    
    if guess == secret_number:
        print "Correct!\n"
        new_game()
    elif remain_guesses == 0:
        print "You ran out of guesses. The number was " + str(secret_number) + "\n"
        new_game()
    elif guess < secret_number:
        print "Higher!\n"
    else:
        print "Lower!\n"
    
# create frame
frame = simplegui.create_frame("Guess the number", 200,200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100, 200)
frame.add_button("Range is [0,1000)",range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
