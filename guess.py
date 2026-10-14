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
    def __init__(self):
        self.completed: bool = False # Flag showing if game was completed or not
        self.target = random.randint(1, 20) # Randomly generate the target to reach
        self.attempts = 0 # Number of attempts recorded
        self.current_guess = None
        self.prev_valid_response = True
        self.won = False

    def prompt_to_answer(self):
        answer = None
        if self.prev_valid_response:
            if self.current_guess == None:
                answer = input("Please input your first guess: ")
            elif self.current_guess > self.target:
                answer = input("Your previous guess was too high! New guess: ")
            else:
                answer = input("Your previous guess was too low! New guess: ")
        else:
            answer = input("Your previous response was invalid, please input only numbers: ")
        return answer

    def validate_response(self, answer:str):
        if answer and answer.isnumeric():
            self.current_guess = int(answer)
            self.attempts += 1
            self.prev_valid_response = True
            return True
        else:
             self.prev_valid_response = False
             return False

    def check_end_condition(self):
        current_condition = self.current_guess == self.target
        self.completed = current_condition
        self.won = True
        return self.completed

    def end_game(self):
        if self.won:
            print(f"YOU WON!!! It took {self.attempts} attempts!")
        else:
            print("YOU LOST!!")


    def game_loop(self):
        while not self.completed:
            answer = self.prompt_to_answer()
            self.validate_response(answer=answer)
            self.check_end_condition()
            pass
        self.end_game()


if __name__ == "__main__":
    game = Game()
    game.game_loop()