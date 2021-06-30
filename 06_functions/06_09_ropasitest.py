import random

class Game:
    
    symbol = ["rock", "paper", "scissor"]
    
    def __init__(self, num):
        self.num = num

    def stringconversion(self):
        self.num = self.symbol[self.num]
        return self.num

    #def show(self):
        #return f"{self.symbol[self.num]}"


class Hand(Game):
    
    def __init__(self, name = "Computer", num = 0):
        self.name = name
        self.num = num
    
    def __str__(self):
        return f"{self.name} chooses {self.num}"

    def random(self):
        self.num = random.randint(0, 2)
        return self.num

    def user_name(self):
        self.name = input("Pls enter your name: ")

    def user_choice(self):
        self.num = int(input("Pls enter number from 0 to 2: "))

# Creating the object (standard would be "Computer chooses rock")
player = Hand()
# Fetch user input
player.user_name()
# Fetch user choice
player.user_choice()
player.stringconversion()
print(player)

computer = Hand()
# get computer random choice
computer.random()
computer.stringconversion()
print(computer)

def determine_winner(player, computer):
    if player == computer:
        return "it's a tie"

    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissor - u win"
        else:
            return "paper covers rock - u loose"

    elif player == "paper":
        if computer == "rock":
            return "paper covers rock - u win"
        else:
            return "scissor cuts paper - u loose"

    elif player == "scissor":
        if computer == "paper":
            return "scissor cuts paper - u win"
        else:
            return "rock smashes scissor - u loose"

print(determine_winner(player.num, computer.num))