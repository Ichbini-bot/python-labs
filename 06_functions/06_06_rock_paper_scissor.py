# need to import random modul
# need to have user input
    # need to have a function that string represents the users input (0 = scissor, 1 = rock, 2 = paper) 
# need to have computer input => here comes random in play
    # need use the function above re string representation
# make function, that compares against: rock beats scissor, scissor beats paper, paper beats rock
# print result
import random
random.seed()

user_input = int(input("enter numbers between 0 and 2: "))

computer_input = random.randint(0,2)

def get_hand(input_data):
    signs = ["rock", "paper", "scissor"]
    return signs[input_data]
    
print("you selected: ", get_hand(user_input))
print("computer selected: ", get_hand(computer_input))

user_input = get_hand(user_input)
computer_input = get_hand(computer_input)   #if i kill these, then tie works - but else it returns none

def determine_winner(user_input, computer_input):
    if user_input == computer_input:
        return "it's a tie"

    elif user_input == "rock":
        if computer_input == "scissor":
            return "rock smashes scissor - u win"
        else:
            return "paper covers rock - u loose"

    elif user_input == "paper":
        if computer_input == "rock":
            return "paper covers rock - u win"
        else:
            return "scissor cuts paper - u loose"

    elif user_input == "scissor":
        if computer_input == "paper":
            return "scissor cuts paper - u win"
        else:
            return "rock smashes scissor - u loose"

print(determine_winner(user_input, computer_input))

