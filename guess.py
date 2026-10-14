import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.

class Game:
    """
    Class to manage the game state
    """
    def __init__(self):
        self.completed: bool = False # Flag showing if game was completed or not
        self.target = random.randint(DEBUG_SECRET) # Randomly generate the target to reach
        self.attempts = 0 # Number of attempts recorded
        self.latest_valid_guess = None # Latest valid guess 
        self.latest_valid_response = True # If latest response was valid or not
        self.won = False # If user won latest game

    def prompt_to_answer(self):
        """
        Prompts the user to answer, initiates separate input prompts based on following:
        1. If this is users first response
        2. If latest response was invalid
        3. If latest response was valid but greater than target
        4. If latest response was valid but lesser than target
        """
        answer = None
        if self.latest_valid_response:
            if self.latest_valid_guess == None:
                answer = input("Please input your first guess: ")
            elif self.latest_valid_guess > self.target:
                answer = input("Your previous guess was too high! New guess: ")
            else:
                answer = input("Your previous guess was too low! New guess: ")
        else:
            answer = input("Your previous response was invalid, please input only numbers: ")
        return answer

    def validate_response(self, answer:str):
        """
        Check if a response is valid and update state accordinly
        """
        if answer and answer.isnumeric():
            self.latest_valid_guess = int(answer)
            self.attempts += 1
            self.latest_valid_response = True
            return True
        else:
             self.latest_valid_response = False
             return False

    def check_end_condition(self):
        """
        Update the state in case the game has reached end conditions
        """
        current_condition = self.latest_valid_guess == self.target
        self.completed = current_condition
        self.won = True
        return self.completed

    def end_game(self):
        """
        Print the end game message depending on end state
        """
        if self.won:
            print(f"YOU WON!!! It took {self.attempts} attempts!")
        else:
            print("YOU LOST!!")


    def game_loop(self):
        """
        Game loop to follow for the playthrough
        """
        while not self.completed:
            answer = self.prompt_to_answer()
            self.validate_response(answer=answer)
            self.check_end_condition()
            pass
        self.end_game()


if __name__ == "__main__":
    game = Game()
    game.game_loop()