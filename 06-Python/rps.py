#!/usr/bin/env python3
"""
This program plays a game of Rock, Paper, Scissors between
two Players, and reports both Player's scores each round.
"""

import random


moves = ['rock', 'paper', 'scissors']


class Output:
    """
    The Output class is responsible for displaying all output to the user.
    """

    def show_banner(self):
        """Shows a pre-defined banner on the output stream."""
        self.show_content("#" * 50)

    def show_line(self, modifier):
        """
        Shows a line

        Parameters:
            modifier (String): a value that is prepended to the line.
        """
        if modifier is None:
            modifier = ""
        self.show_content(modifier + ("-" * 30))

    def show_content(self, content):
        """
        Shows content on the output stream.

        Parameters:
            content (string): The content to be displayed.
        """
        print(content)

    def show_strategy_menu(self):
        """Prints the game strategy selection menu"""
        self.show_content("Please select a strategy for your opponent "
                          "from the numbered list.")
        self.show_content("\t1 - The Rock: always plays 'rock'")
        self.show_content("\t2 - You'll never guess!")
        self.show_content("\t3 - Monkey see, monkey do: "
                          "repeats every move you play!")
        self.show_content("\t4 - The Cylist: cycles through "
                          "the moves in ordered manner.")
        self.show_line(None)


class Player:
    """
    The Player class is the parent class for all of the Playersin this game.
    """

    def move(self):
        """Plays the same move everytime."""
        return 'rock'

    def learn(self, my_move, their_move):
        """
        The implementation of the learn function is delegated to
        any subclass that chooses to implement it.
        """
        pass

    def name(self):
        return "Computer"


class RandomPlayer(Player):
    """The RandomPlayer class plays a random move each turn."""

    def move(self):
        """The RandomPlayer implementation plays a random move."""
        return random.choice(moves)


class HumanPlayer(Player):
    """The HumanPlayer class prompts for a move from the input stream."""

    def move(self):
        """
        Prompts the user for a move and validates the input
        Continues to prompt until a valid input is received.
        """
        while True:
            my_move = input("Rock, paper, scissors? > ").lower().strip()
            if self.is_valid_move(my_move):
                break
        return my_move

    def is_valid_move(self, my_move):
        """
        Validates a move is in the list of moves for the game.

        Parameters:
            my_move (string): The move to validate.

        Returns:
            Boolean: True if the move is valid, otherwise false.
        """
        return my_move in moves

    def name(self):
        return "Player"


class ReflectPlayer(Player):
    """
    The ReflectPlayer class always repeats the last
    move of the opposing player.
    """

    def __init__(self):
        """
        The instance is initialized with a random move in case the
        ReflectPlayer is the first player to move.
        """
        self.my_move = random.choice(moves)

    def move(self):
        """Plays the move stored in its instance variable."""
        return self.my_move

    def learn(self, my_move, their_move):
        """
        Stores the opponent's move in an instance variable so
        it can be played for the next round.

        Parameters:
            my_move (string): The move this player made for the current round.
            their_move (string): The opposing player's move for the
            current round.
        """
        self.my_move = their_move


class CyclePlayer(Player):
    """
    The CyclePlayer class remembers the move it played last round
    and plays the next move in the list for the current round.
    """

    def __init__(self):
        """
        The instance is initialized to 'Rock' to cover the case
        where the instance has the first move of the game.
        """
        self.move_index = 0

    def move(self):
        """Plays the move stored in its instance variable."""
        return moves[self.move_index]

    def learn(self, my_move, their_move):
        """
        Evaluate the move played this round and store the next
        move to be played. Cycle back to the beginning of the list
        as necessary.

        Parameters:
            my_move (string): The move this player made for the current round.
            their_move (string): The opposing player's move for
            the current round.
        """
        self.move_index = 0 if self.move_index == 2 else self.move_index + 1


def beats(one, two):
    """
    Determines the winning move between two moves played.

    Parameters:
        one (string): A move to evaluate.
        two (string): The second move to evaluate.

    Returns:
        Boolean: True if one beats two, otherwise False.
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """
    The Game class controls the game and keeps track of rounds
    played and who wins each round

    Attributes:
        p1 (Player): an instance of a Player class to represent player 1.
        p2 (Player): an instance of a Player class to represent player 2.
        output (Output): an instance of the Output class to show output.
    """

    def __init__(self, p1, p2, output):
        """
        Instance variables are initialized and persisted.

        Parameters:
            p1 (Player): an instance of a Player class to represent player 1.
            p2 (Player): an instance of a Player class to represent player 2.
            output (Output): an instance of the Output class to show output.
        """
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds_to_play = 0
        self.rounds_played = 0
        self.output = output
        self.number_ties = 0

    def show_welcome(self):
        """Shows a welcome message to the user."""
        self.output.show_content("\n")
        self.output.show_banner()
        self.output.show_content("Welcome to Rock, Paper, Scissors!")
        self.output.show_banner()
        self.output.show_content("\n")

    def ask_strategy(self):
        """
        Asks the player which strategy they would like to play.

        Returns:
            Player: an instance of the Player type chosen by the player
        """
        self.output.show_strategy_menu()
        while True:
            strategy = input("Select a strategy 1-4: ")
            if(strategy.isdigit()):
                strategy = int(strategy)
                if strategy == 1:
                    return Player()
                elif strategy == 2:
                    return RandomPlayer()
                elif strategy == 3:
                    return ReflectPlayer()
                elif strategy == 4:
                    return CyclePlayer()

    def randomize_first_player(self):
        """Randomly selects the first player."""
        rnd = random.randint(1, 10)
        if rnd >= 5:
            # Switch p1 and p2
            self.p1 = type(self.p2)()
            self.p2 = HumanPlayer()

    def ask_number_rounds(self):
        """
        Asks how many rounds should be played. Repeats until valid
        numeric entry is received.

        Returns:
            Int: the number of rounds to be played.
        """
        while True:
            rounds = input("How many rounds would you like to "
                           " play [0-10]? ".strip())
            if(rounds.isdigit()):
                rounds = int(rounds)
                if rounds >= 0 and rounds <= 10:
                    return int(rounds)

    def score_round(self, p1_move, p2_move):
        """
        Scores a round and stores each player's score in
        an instance variable.

        Parameters:
            p1_move (string): the move played by player 1
            p2_move (string): the move played by player 2
        """
        if beats(p1_move, p2_move):
            self.p1_score += 1
            return f"** {self.p1.name().upper()} WINS! **"
        elif beats(p2_move, p1_move):
            self.p2_score += 1
            return f"** {self.p2.name().upper()} WINS! **"
        else:
            self.number_ties += 1
            return "** TIE GAME! **"

    def show_game_outcome(self, winner):
        """
        Shows the outcome of the game and announces the winner.

        Parameters:
            winner (string): The name of the winning player
        """
        self.output.show_content("\n")
        self.output.show_banner()
        if winner is None:
            self.output.show_content("Game Over")
        else:
            self.output.show_content(f"Game Over: {winner} wins the game!")
        self.output.show_content("Final scores:")
        self.output.show_content(f"\t{self.p1.name()}: ".ljust(15) +
                                 f"{self.p1_score} rounds")
        self.output.show_content(f"\t{self.p2.name()}: ".ljust(15) +
                                 f"{self.p2_score} rounds")
        self.output.show_content(f"\tTies: ".ljust(15) +
                                 f"{self.number_ties} rounds")
        self.output.show_line("\t")
        self.output.show_content("\tTotal rounds: ".ljust(15) +
                                 f"{self.rounds_played}")
        self.output.show_banner()

    def show_score(self):
        """Shows the current score of each player."""
        self.output.show_content(f"Score: {self.p1.name()}: "
                                 f"{self.p1_score}, "
                                 f"{self.p2.name()}: {self.p2_score}")

    def play_round(self):
        """Plays a round of the game and shows the outcome."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.output.show_content(f"{self.p1.name()}: {move1}  "
                                 f"{self.p2.name()}: {move2}")

        self.output.show_content(self.score_round(move1, move2))
        self.show_score()

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def determine_game_winner(self):
        """
        Determines who is the game winner.

        Returns:
            String: The name of the winning player, or None if there isn't
            a winner.
        """
        if self.p1_score > self.p2_score:
            return self.p1.name()
        elif self.p2_score > self.p1_score:
            return self.p2.name()

    def play_game(self):
        """
        Launches the game and continues playing rounds until a winner
        is determined.
        """
        self.show_welcome()
        self.p2 = self.ask_strategy()
        self.randomize_first_player()
        self.rounds_to_play = self.ask_number_rounds()
        self.output.show_content("Go!")
        winner = None
        while self.rounds_played < self.rounds_to_play:
            self.rounds_played += 1
            self.output.show_content(f"\nRound {self.rounds_played}:")
            self.play_round()

        winner = self.determine_game_winner()
        self.show_game_outcome(winner)


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player(), Output())
    game.play_game()
