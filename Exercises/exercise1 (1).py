"""A very basic card game"""

print('**********Card Busters**********\n')

player_1 = [10, 6, 8, 9, 7, 12, 7]
player_2 = [7, 6, 9, 5, 2, 8, 11]

player_1_score = 0
player_2_score = 0

for i in range(0, len(player_1)):

    print('Round number ', i + 1, ':', sep='', end='')
    if player_1[i] > player_2[i]:
        print(' Player 1 wins the round, with', player_1[i], 'beating', player_2[i]) 
        player_1_score += 1
    elif player_2[i] > player_1[i]:
        print(' Player 2 wins the round, with', player_2[i], 'beating', player_1[i]) 
        player_2_score += 1
    else:
        print(' This round has ended in a draw')
        

if player_1_score > player_2_score:
    print('\nPlayer 1 wins the game, by', player_1_score, 'wins to', player_2_score)
elif player_2_score > player_1_score:
    print('\nPlayer 2 wins the game, by', player_2_score, 'wins to',  player_1_score)
else:
    print('\nThe whole game was tied:', player_1_score, '-', player_2_score)
