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
        self.attempts = 0 # Number of attempts recorded
        self.latest_valid_guess = None # Latest valid guess 
        self.latest_valid_response = True # If latest response was valid or not
        self.won = False # If user won latest game
        self.first_guess = True # If this will be the first guess user will take in the game
        self.level_name = None # Level requested name
        self.max_range = None # Max val of target
        self.min_range = None # Min val of target 
        self.target = None # Randomly generate the target to reach
        self.max_attempts = None # Max attempts allowed
        self.start_time = None
        self.current_time = None
        self.mode = None
        self.timed_mode = False

    def prompt_mode_request(self):
            """
            Requests user to respond with the mode they want and only calls the setter on valid ones
            """
            requested = input("Please respond with the mode you choose | 1 for Classic Challenge or 2 for Time Challenge: ")
            if requested.isnumeric():
                requested = int(requested)
            else:
                pass
            if requested == 1:
                self.set_mode(name="Classic Challenge")
            elif requested == 2:
                self.set_mode(name="Time Challenge")
                self.timed_mode = True
            else:
                pass

    def set_mode(self, name: str):
        """
        Set the mode requested
        """
        self.mode = name

    def confirm_mode_message(self):
        """
        Message to confirm the mode selected to the user!
        """
        print(f"You have requested {self.mode} mode!")
        if self.timed_mode:
            print(f"You will get {TIME_LIMIT} seconds!!")

    def prompt_level_request(self):
        """
        Requests user to respond with the level they want and only calls the setter on valid ones
        """
        requested = input("Please respond with the level you choose | 1 for Easy, 2 for Medium, or 3 for Hard: ")
        if requested.isnumeric():
            requested = int(requested)
        else:
            pass
        if requested == 1:
            self.set_level(name="Easy", min_range=1, max_range=50, max_attempts=10)
        elif requested == 2:
            self.set_level(name="Medium", min_range=1, max_range=100,  max_attempts=8)
        elif requested == 3:
            self.set_level(name="Hard", min_range=1, max_range=500, max_attempts=10)
        else:
            pass

    def set_level(self, name:str, min_range: int, max_range: int, max_attempts: int):
        """
        Sets the level requested
        """
        self.level_name = name
        self.max_range = max_range
        self.min_range = min_range
        self.max_attempts = max_attempts
        self.target = random.randint(self.min_range, self.max_range)

    def confirm_level_message(self):
        """
        Prints a message to user confirming their level selection, max attempts, and range
        """
        print(f"User has selected the following: \nLevel: {self.level_name}\n Max Range: {self.max_range} \n You get Max {self.max_attempts} attempts!")

    def prompt_to_answer(self):
        """
        Prompts the user to answer, initiates separate input prompts based on following:
        1. If this is users first response
        2. If latest response was invalid
        3. If latest response was valid but greater than target
        4. If latest response was valid but lesser than target
        """
        answer = None
        print(f"{self.max_attempts - self.attempts} attempts left!!")
        if self.first_guess:
            answer = input("Please input your first guess: ")
            self.first_guess = False
            return answer
        if self.latest_valid_response:
            if self.latest_valid_guess > self.target:
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
        if self.latest_valid_guess == self.target:
            self.completed = True
            self.won = True
        elif self.max_attempts <= self.attempts:
            self.completed = True
            self.won = False
        return self.completed

    def end_game(self):
        """
        Print the end game message depending on end state
        """
        if self.won:
            print(f"YOU WON!!! It took {self.attempts} attempts!")
        else:
            print(f"YOU LOST!! You have exceeded the {self.max_attempts} attempts allowed!\n THE SECRET NUMBER WAS: {self.target}")


    def game_loop(self):
        """
        Game loop to follow for the playthrough
        """
        while not self.mode:
            self.prompt_mode_request()
        self.confirm_mode_message()
        while not self.level_name:
            self.prompt_level_request()
        self.confirm_level_message()
        while not self.completed:
            answer = self.prompt_to_answer()
            self.validate_response(answer=answer)
            self.check_end_condition()
            pass
        self.end_game()


if __name__ == "__main__":
    game = Game()
    game.game_loop()