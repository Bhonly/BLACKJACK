# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

mytotal = draw_starting_hand("YOUR TURN")
user_total = 0
print_end_turn_status(mytotal)
while mytotal < 21:        
   que = input('You have ' + str(mytotal) + ". Hit (y/n)? ")
   if que == 'n':
        print("Final hand: " + str(mytotal) + '.')
        user_total = mytotal
        mytotal = mytotal + 21
   elif que == 'y':
        new_card = draw_card()
        mytotal = mytotal + new_card
        user_total = mytotal  
   else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_total)  
mytotal = user_total


dealertotal = draw_starting_hand('DEALER TURN')
while dealertotal < 17:
   print("Dealer has " + str(dealertotal) + '.')
   new_card = draw_card()
   dealertotal = dealertotal + new_card
if dealertotal >= 17 and dealertotal < 21:
   print("Final hand: " + str(dealertotal) + '.')   
print_end_turn_status(dealertotal)   


print_end_game_status(mytotal, dealertotal)



