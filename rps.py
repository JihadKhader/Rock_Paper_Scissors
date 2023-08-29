
import random

color_player1 = '\033[91m'  
color_player2 = '\033[94m'  
color_reset = '\033[0m'

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

class Player:
    def move(self):
        return 'rock'



    def learn(self, my_move, their_move):
        pass



def beats(one, two):
    return ((one == 'rock' and (two == 'scissors' or two == 'lizard')) or
            (one == 'scissors' and (two == 'paper' or two == 'lizard')) or
            (one == 'paper' and (two == 'rock' or two == 'spock')) or
            (one == 'spock' and (two == 'scissors' or two == 'rock')) or
            (one == 'lizard' and (two == 'spock' or two == 'paper')))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2



    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {color_player1}{move1}{color_reset}"
    "Player 2: {color_player2}{move2}{color_reset}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)



    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()

        print("Game over!")

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock,"
    "paper, scissors, spock, lizard): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move. Please try again.")

if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors Spock Lizard!")
    opponent_choice = input("Do you want to "
"play against the computer "
"or against another player? (computer / player): ").lower()

    if opponent_choice == "computer":
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif opponent_choice == "player":
        game = Game(HumanPlayer(), HumanPlayer())
        game.play_game()
    else:
        print("Invalid choice. Please choose 'computer' or 'player'.")
