# Number Guessing Game

A simple command-line interface (CLI) based Number Guessing Game built with Go. The game generates a random number between 1 and 100, and the player must guess the number within a limited number of attempts based on the selected difficulty level.

## Features

- **Difficulty Levels**: Choose from Easy, Medium, and Hard levels, each with a different number of attempts.
- **Interactive Gameplay**: Receive hints if the guess is too high or too low.
- **Exit Anytime**: Type `-1` at any prompt to quit the game.
- **Attempts Tracking**: Tracks and displays the number of remaining attempts.

## Getting Started

### How to Play

1. When the game starts, you will see a welcome message and be prompted to select a difficulty level:

   - **Easy**: 10 attempts
   - **Medium**: 5 attempts
   - **Hard**: 3 attempts

2. Enter your choice (1 for Easy, 2 for Medium, 3 for Hard).

3. Enter your guesses when prompted. The game will guide you if the guess is too high or too low.

4. The game ends when:
   - You guess the correct number (you win).
   - You run out of attempts (you lose).

### Sample Gameplay

```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter -1 to quit the game at any time.

Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!

Attempt 1/5 - Enter your guess: 50
Incorrect! The number is less than 50.

Attempt 2/5 - Enter your guess: 25
Incorrect! The number is greater than 25.

Attempt 3/5 - Enter your guess: 30
Congratulations! You guessed the correct number in 3 attempts.
```
