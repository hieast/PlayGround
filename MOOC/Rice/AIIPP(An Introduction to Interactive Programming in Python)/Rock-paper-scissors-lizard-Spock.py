import random
def rpsls(player_choice): 
    '''
    print player's and computer's choose, and show who wins.
    '''
    
    #use dic to convert name to num
    #with the help of dic, it's no need to implement helper functions
    name2num = {'rock':0, 'Spock':1, 'paper':2, 
                'lizard':3, 'scissors':4}
    computer_choice = random.choice(name2num.keys())
    test_num = (name2num[computer_choice]-name2num[player_choice])%5
    
    #print choice
    print "Player chooses " + player_choice
    print "Computer chooses " + computer_choice
    
    #print winner message
    if test_num > 2:
        print "Player wins!\n"
    elif test_num > 0:
        print "Computer wins!\n"
    else:
        print "Player and computer tie!\n"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


