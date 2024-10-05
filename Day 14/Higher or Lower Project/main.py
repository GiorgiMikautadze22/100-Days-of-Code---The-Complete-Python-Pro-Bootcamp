#TODO: take 2 random celebrities from the data
#TODO: Ask the user to guess which has more followers
#TODO: Create function that compares and returns the which celebrity won
#TODO: If the users guess equals to the output of the compare function then increase score count.
#TODO: Else stop the game and print the score.
#TODO: Write a while loop that keeps asking higher or lower until game is over
#TODO: After the game has ended ask the user if he wants to play again.

import random
import game_data

def compare(celeb_1, celeb_2):
    if celeb_1["follower_count"] > celeb_2["follower_count"]:
        return 1
    else:
        return 2

def higher_lower():
    score = 0
    game_over = False
    celeb_1 = random.choice(game_data.data)
    celeb_2 = random.choice(game_data.data)

    while not game_over:
        user_guess = int(input(f'Who has more followers {celeb_1["name"]} or {celeb_2["name"]}. Write "1" or "2" \n'))

        if user_guess == compare(celeb_1, celeb_2):
            score += 1
            if user_guess == 1:
                celeb_2 = random.choice(game_data.data)
            else:
                celeb_1 = random.choice(game_data.data)
            print(f'You are correct. Your score {score}')
        else:
            print(f'You lost. Your score {score}')
            game_over = True

    play_again = input('Do you want to play again? y or n: ')
    if play_again == 'y':
        higher_lower()
    else:
        print('Good by')

higher_lower()
