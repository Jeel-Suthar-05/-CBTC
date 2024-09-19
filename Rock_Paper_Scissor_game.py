import random


class RockPaperScissors:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
        self.outcomes = {
        ("rock", "scissors"): "rock",
        ("scissors", "paper"): "scissors",
        ("paper", "rock"): "paper"
        }

    def determine_winner(self):
        if self.player1 == self.player2:
            return "It's a tie!"
        
        if (self.player1, self.player2) in self.outcomes:
            return f"Player 1 wins! \n{self.player1} beats {self.player2}."
        else:
            return f"Player 2 wins! \n{self.player2} beats {self.player1}."


player1 = input("Player 1, enter rock, paper, or scissors: ").lower()

# Generate a random choice for the computer
choices = ["rock", "paper", "scissors"]
player2 = random.choice(choices)

print(f"Computer chose: {player2}")

# Example usage
game = RockPaperScissors(player1, player2)
result = game.determine_winner()
print(result)

