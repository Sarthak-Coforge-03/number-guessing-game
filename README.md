# number-guessing-game

## Test Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---------------|------------|-----------------|---------------|-------|
| 1 | Guess too low | Secret is 42; guess 41 | Your previous guess was too low! New guess: | Your previous guess was too low! New guess: | Yes |
| 2 | Guess too high | Secret is 42; guess 43 | Your previous guess was too high! New guess: | Your previous guess was too high! New guess: | Yes |
| 3 | Correct guess and attempt count | Secret is 42; guess 41, then 43, then 42 | "YOU WON!!! It took 3 attempts!" | YOU WON!!! It took 3 attempts! | Yes |
| 4 | Letters as input | Enter `abc` as a guess | Rejected as invalid; attempts didn't change | 10 attempts left!!<br>Your previous response was invalid, please input only valid numbers: | Yes |
| 5 | Blank entry | Press Enter without typing anything | Rejected as invalid; attempts didn't change | 10 attempts left!!<br>Your previous response was invalid, please input only valid numbers: | Yes |
| 6 | Number below range | Enter `0` on Easy (range 1-50) | Rejected as invalid; attempts didn't change | 10 attempts left!!<br>Your previous response was invalid, please input only valid numbers: | Yes |
| 7 | Number above range | Enter `51` on Easy (range 1-50) | Rejected as invalid; attempts didn't change | 10 attempts left!!<br>Your previous response was invalid, please input only valid numbers: | Yes |
| 8 | Running out of attempts | Choose Classic mode; make only wrong valid guesses until attempts are used up | "YOU LOST!!" message with the secret number | YOU LOST!! You have exceeded the 10 attempts allowed!<br>THE SECRET NUMBER WAS: 42 | Yes |
| 9 | Timeout in Time Challenge | Choose Time Challenge (mode 2); wait past 60 seconds, then submit a guess | "YOU LOST!!" message with the secret number | YOU LOST!! You have exceeded the 60 seconds limit!<br>THE SECRET NUMBER WAS: 42 | Yes |
| 10 | Remaining time shown before each guess | In Time Challenge, make several guesses | "You have N seconds left!!" printed before every guess prompt after the first | You have 15 seconds left!!<br>7 attempts left!!<br>Your previous guess was too low! New guess: 9 | Yes |
| 11 | Choose Easy mode | In Time Challenge, make several guesses | User selection, max range, and max attempts shown | User has selected the following:<br>Level: Easy<br>Max Range: 50<br>You get Max 10 attempts! | Yes |
| 12 | Choose Medium mode | In Time Challenge, make several guesses | User selection, max range, and max attempts shown | User has selected the following:<br>Level: Medium<br>Max Range: 100<br>You get Max 8 attempts! | Yes |
| 13 | Choose Hard mode | In Time Challenge, make several guesses | User selection, max range, and max attempts shown | User has selected the following:<br>Level: Hard<br>Max Range: 500<br>You get Max 10 attempts! | Yes |
