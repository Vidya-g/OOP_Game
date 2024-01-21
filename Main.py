from Player import Player
from Question import Question
from Game import Game

# Create players
player1 = Player("Player 1")


# Create questions
question1 = Question("What is the capital of India?", ["A. Delhi", "B. Mumbai", "C. Karnataka"], "A")


game= Game(player1, question1)
game.play_game()
