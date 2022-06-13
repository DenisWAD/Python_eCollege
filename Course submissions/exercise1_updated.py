"""This is a simple 2-player card fame....Have fun playing!"""

#Player hands
p1_cards = [10, 6, 8, 9, 7, 12, 7]
p2_cards = [7, 6, 9, 5, 2, 8, 11]

#Keep track of each players wins and draws
p1_wins = 0
p2_wins = 0
draws = 0

#Keep track of round number
round_num = 0

def play_game() :
    """This function plays all the game rounds, printing out the winner of each round"""
    #Main game loop
    global round_num, p1_wins, p2_wins, draws
    for i in p1_cards :
        
        if p1_cards[round_num] == p2_cards[round_num]:
            print("Round Number", round_num + 1, ": This round ended in a draw") # This prints out the round number of each round
            draws += 1
        elif p1_cards[round_num] > p2_cards[round_num]:
            print("Round Number", round_num + 1, ": Player 1 wins the round, with ", p1_cards[round_num], "beating", p2_cards[round_num] )
            p1_wins += 1
        elif p1_cards[round_num] < p2_cards[round_num]:
            print("Round Number", round_num + 1, ": Player 2 wins the round, with ", p2_cards[round_num], "beating", p1_cards[round_num] )
            p2_wins += 1
            
        round_num += 1


def final_result() :
    """This function lets the game players know who won the overall game"""
    #Output results
    if p1_wins > p2_wins and p1_wins > draws:
        print("\nPlayer 1 wins the game, by", p1_wins, "wins to", p2_wins)
    elif p2_wins > p1_wins and p2_wins > draws :
        print("\nPlayer 2 wins the game, by", p2_wins, "wins to", p1_wins)
    else :
        print("The game ended in a draw")


def future_enhancements() :
    """Nothing to see here"""
    
    pass


play_game()
final_result()