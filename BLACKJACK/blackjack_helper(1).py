# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    if card_rank == 1:
      value = 11
      x = "Ace"
      print("Drew an " + x)
    elif card_rank == 11:
      value = 10
      x = 'Jack'  
      print("Drew a " + x)
    elif card_rank == 12:
      value = 10
      x = 'Queen'
      print("Drew a " + x)
    elif card_rank == 13:
      value = 10
      x = 'King'
      print("Drew a " + x)
    else:
      x = str(card_rank)
      if card_rank == 8:
        value = card_rank
        print("Drew an " + x)
      elif card_rank >= 2 and card_rank <= 10:
        value = card_rank
        print("Drew a " + x)
      else:
        print("BAD CARD")
# Implement card_name function here
# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
  
def draw_card():
   num = randint(1, 13)
   print_card_name(num)
   if num == 1:
      value = 11
   elif num == 11:
      value = 10    
   elif num == 12:
      value = 10    
   elif num == 13:
      value = 10   
   else:
      value = num
   return value
# Implement draw_card function here

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
   
def print_header(message):
    if message == 'YOUR TURN':
        print('-----------\nYOUR TURN\n-----------')
    elif message == "DEALER TURN":
        print("-----------\nDEALER TURN\n-----------")
    elif message == 'GAME RESULT':    
        print("-----------\nGAME RESULT\n-----------")
    else:
        print('-----------\n{} TURN\n-----------'.format (message))        
# Implement print_header function here

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
   print_header(name) 
   firstcard = draw_card()
   secondcard = draw_card()
   total = firstcard + secondcard  
   return total      
# Implement draw_starting_hand function here

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value): 
    if hand_value == 21:
        print("Final hand: {}".format(str(hand_value)))   
        print("BLACKJACK!")
    elif hand_value > 21:
        print("Final hand: {}".format(str(hand_value)))  
        print("BUST.")
    return hand_value        
         
   


       
    # Implement print_end_turn_status function here

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
 print_header('GAME RESULT') 
 if user_hand > 21:
    print("Dealer wins!")
 if dealer_hand > user_hand and dealer_hand <= 21:
    print("Dealer wins!")
 if user_hand > dealer_hand and user_hand <= 21:
    print("You win!")
 if user_hand == dealer_hand and user_hand <= 21:
    print("Push.")
 if dealer_hand > 21 and user_hand < 21:
    print("You win!")
 if user_hand == dealer_hand and dealer_hand > 21:
    print("Dealer wins!")  
    # Implement print_end_game_status function here
