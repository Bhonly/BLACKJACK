from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    def test_example(self, input_mock, randint_mock):
     #The user receives cards that end up with a hand less than 21.
     #The dealer wins by having a higher hand, an exact value of 21, than the user.
        output = run_test([1,3,5], ['y', 'y', 'n'], [5,6,12])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 5\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand more than 21, which is a Bust.
        #The dealer wins by having a value less than 21, which prevents it from getting Bust.
        output = run_test([1,3,12], ['y', 'y'], [5,6,7])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 5\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew  a Queen"
                   "Final hand: 29.\n"
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew a 7\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_userbusts_dealerwins(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand more than 21, making him Bust.
        #The dealer wins since the user is already bust. Although the dealer has a value also more than 21.
        output = run_test([5,1,12], ['y', 'y', 'y'], [5,8,13])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an Ace\n" \
                   "You have 16. Hit (y/n)? y\y" \
                   "Drew a Queen\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n"
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew a King\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n"
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealerwins(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand less than 21.
        #The dealer wins by having a blackjack value which is equal to 21. 
        output = run_test([1,3,5], ['y', 'y', 'n'], [5,6,7])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 5\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealerbusts_userwins(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand less than 21.
        #The dealer loses to the user since the dealer has a value more than 21, which is a Bust, while the user has a blackjack, a value equal to 21.
        output = run_test([1,3,7], ['y'], [5,8,12])
        expected = "-----------\n" \
                   "YOUR TURN\n" 
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew a Queen\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n" \
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def dealerwins_dealeronblackjack(self, input_mock, randint_mock):            
        #The user receives cards that end up with a hand less than 21.
        #The dealer wins by having a blackjack value which is equal to 21.
        output = run_test([1,3,5], ['y', 'n'], [5,6,1])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 5\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealerloses_user_greater_than_dealer(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand less than 21.
        #The dealer losses to the user by having the less value than the user.
        output = run_test([1,3,5], ['y', 'n'], [3,5,10])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\y" \
                   "Drew an 5\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_both_less_than_21(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand less than 21.
        #This is a Push since the dealer has the same value which is also less than 21.
        output = run_test([13,9], ['n'], [13,9])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 9\n" \
                   "Dealer has 19.\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_dealer_on_blackjack(self, input_mock, randint_mock):           
        #The user receives cards that end up with a hand less than 21.
        #The dealer wins by having a higher hand, an exact value of 21, than the user.
        output = run_test([1, 1], [[1, 13])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \            
                   "Final hand: 18.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_both_on_blackjack(self, input_mock, randint_mock):           
        #The user receives cards that end up with a number that equals 21.
        #This is a Push since the dealer has the same value which is also equal to 21.
        output = run_test([1, 13], [[1, 13])
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \            
                   "Final hand: 21.\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n" 
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()

             



