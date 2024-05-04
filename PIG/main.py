import random

def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number between 1-4: ")
    if players.isdigit():
        players = int(players)
        if 2<=players <=4:
            break
        else:
            print("it must be greater than 2")

    else:
        print("Invalid try again")


max_score = 50
players_score = [0 for _ in range(players)]
# print(players_score)

while max(players_score) < max_score:

    for player_idx in range(players):
        print("\n Player ",player_idx+1," turn started")
        print("Your total score is: ",players_score[player_idx],'\n')
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y or n): ").lower()
            if should_roll != 'y':
                break

            value = roll()
            if value ==1:
                current_score=0
                print("you roll 1, you done!")
            else:
                current_score+=value
                print("you roll ",value)
            
            print("your current score is: ",current_score)

            players_score[player_idx]+=current_score
        print("Your total score is: ",players_score[player_idx])


max_score = max(players_score)
winning_idx = players_score.index(max_score)
print("player number: ",winning_idx+1,"is the winner with the score of ",max_score)