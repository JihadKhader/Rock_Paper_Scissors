import random

color_player1 = '\033[91m'
color_player2 = '\033[94m'
color_reset = '\033[0m'

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']


class Player:
    def __init__(self):
        self.score = 0



    def move(self):
        return 'rock'



    def learn(self, my_move, their_move):
        pass


class Game:


    def __init__(self, p1, p2, rounds = 3):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds
        self.round_scores = []



    def play_round(self, round_num):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {color_player1}{move1}{color_reset} "
                f"Player 2: {color_player2}{move2}{color_reset}")

        if move1 == move2:
            print("It's a tie!")
            self.round_scores.append((0, 0))
        elif beats(move1, move2):
            print("Player 1 wins!")
            self.p1.score += 1
            self.round_scores.append((1, 0))
        else:
            print("Player 2 wins!")
            self.p2.score += 1
            self.round_scores.append((0, 1))

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)



    def play_game(self):
        print("Game start!")
        for round_num in range(self.rounds):
            print(f"Round {round_num + 1}:")
            self.play_round(round_num)
            p1_round_score, p2_round_score = self.round_scores[round_num]
            print(f"Round {round_num + 1} scores - "
                    f"Player 1: {p1_round_score}, Player 2: {p2_round_score}")
            print()

        print("Game over!")
        print(f"Final score: Player 1"
" - {self.p1.score}, Player 2 - {self.p2.score}")


def beats(one, two):
    return ((one == 'rock' and (two == 'scissors' or two == 'lizard')) or
            (one == 'scissors' and (two == 'paper' or two == 'lizard')) or
            (one == 'paper' and (two == 'rock' or two == 'spock')) or
            (one == 'spock' and (two == 'scissors' or two == 'rock')) or
            (one == 'lizard' and (two == 'spock' or two == 'paper')))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class AlwaysRockPlayer(Player):
    def move(self):
        return 'rock'



    def learn(self, my_move, their_move):
        pass


class ImitatorPlayer(Player):
    def __init__(self):
        super().__init__()
        self.previous_human_move = None



    def move(self):
        if self.previous_human_move is None:
            return random.choice(moves)
        return self.previous_human_move



    def learn(self, my_move, their_move):
        if their_move in moves:
            self.previous_human_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.move_index = 0



    def move(self):
        move = moves[self.move_index]
        self.move_index = (self.move_index + 1) % len(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock"
", paper, scissors, spock, lizard): ").lower()
            if move in moves:
                return move
            else:
                print("Invalid move. Please try again.")


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors Spock Lizard!")
    opponent_choice = input("Do y"
"ou want to play against the computer o"
"r against another player? (computer / player): ").lower()

    if opponent_choice == "computer":
        strategies = [RandomPlayer(), AlwaysRockPlayer(),
ImitatorPlayer(), CyclePlayer()]
        rounds = int(input("Enter the number of rounds: "))
        game = Game(HumanPlayer(), random.choice(strategies), rounds = rounds)
        game.play_game()
    elif opponent_choice == "player":
        rounds = int(input("Enter the number of rounds: "))
        game = Game(HumanPlayer(), HumanPlayer(), rounds = rounds)
        game.play_game()
    else:
        print("Invalid choice. Please choose 'computer' or 'player'.")
