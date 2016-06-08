# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
is_win = ""
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # compute the value of the hand assume ace as 1
        value = 0
        has_ace = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        # if the hand has an ace,add 10 to hand value if it doesn't bust
        if has_ace and value < 12:
            value += 10
        return value
      
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        hand_loc = [pos[0], pos[1]]
        for card in self.cards:
            card.draw(canvas, hand_loc)
            hand_loc[0] += 100
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in SUITS: 
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        return str(self.deck)

#define help functions
def win():
    global outcome, is_win, in_play, score
    outcome = "New deal?"
    is_win = "You win!"
    in_play = False
    score += 1
    
def lose():
    global outcome, is_win, in_play, score
    outcome = "New deal?"
    is_win = "You lose!"
    in_play = False
    score -= 1

#define event handlers for buttons
def Restart():
    global score, in_play
    score = 0
    in_play = False
    deal()
    

def deal():
    global outcome, is_win, in_play, dealer, player, deck
    
    #Pressing the "Deal" button in the middle of the round causes the player to lose the current round.
    if in_play:
        lose()
        return
    
    outcome = "Hit or stand?"
    is_win = ""
    in_play = True
    
    dealer = Hand()
    player = Hand()
    deck = Deck()
    deck.shuffle()
    
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    

def hit():
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
        # if busted, player lose
        if player.get_value() > 21:
            lose()
        
def stand():
    global outcome, in_play, dealer, player, deck
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21 or dealer.get_value() < player.get_value():
            win()
        else:
            lose()
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    player.draw(canvas, [50, 400])
    dealer.draw(canvas, [50, 200])
    
    canvas.draw_text("score: " + str(score), [400, 100], 36,'White')
    canvas.draw_text("Blackjack", [100, 100], 48, 'Aqua')
    
    
    canvas.draw_text("Dealer", [50, 180], 36, 'Black')
    canvas.draw_text(is_win, [200, 180], 36, 'Black')
    canvas.draw_text("Player", [50, 380], 36, 'Black')
    canvas.draw_text(outcome, [200, 380], 36, 'Black') 
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, 
                          [CARD_CENTER[0] +50, CARD_CENTER[1] + 200], CARD_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Restart", Restart, 200)
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric