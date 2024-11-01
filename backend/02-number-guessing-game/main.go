package main

import (
	"fmt"
	"math/rand"
	"os"
)

func showWelcomeMessage() {
	fmt.Println("Welcome to the Number Guessing Game!")
	fmt.Println("I'm thinking of a number between 1 and 100.")
	fmt.Println()
	fmt.Println("Please select the difficulty level:")
	fmt.Println("1. Easy (10 chances)")
	fmt.Println("2. Medium (5 chances)")
	fmt.Println("3. Hard (3 chances)")
	fmt.Println()
	fmt.Println("Enter -1 to quit the game at any time.")
	fmt.Println()
}

func getChances() int {
	difficultyNames := [3]string{"Easy", "Medium", "Hard"}
	difficultyChances := [3]int{10, 5, 3}

	var difficultyChoice int

	for {
		fmt.Print("Enter your choice: ")
		fmt.Scan(&difficultyChoice)
		fmt.Println()

		// Check for exit option
		if difficultyChoice == -1 {
			fmt.Println("Exiting the game. Goodbye!")
			os.Exit(0)
		}

		// Validate choice
		if difficultyChoice >= 1 && difficultyChoice <= 3 {
			fmt.Printf("Great! You have selected the %s difficulty level.\n", difficultyNames[difficultyChoice-1])
			fmt.Println("Let's start the game!")
			fmt.Println()
			return difficultyChances[difficultyChoice-1]
		}
		fmt.Println("Invalid choice. Please select a valid difficulty level (1, 2, or 3).")
		fmt.Println()
	}
}

func startGame(chances int, targetNumber int) {
	for attempt := 1; attempt <= chances; attempt++ {
		var userGuess int
		fmt.Printf("Attempt %d/%d - Enter your guess: ", attempt, chances)
		fmt.Scan(&userGuess)

		// Exiting in the middle of game
		if userGuess == -1 {
			fmt.Println("Exiting the game. Goodbye!")
			os.Exit(0)
		}

		// Checking guess
		if targetNumber == userGuess {
			fmt.Printf("Congratulations! You guessed the correct number in %d attempts.\n", attempt)
			return
		}

		// Providing feedback
		if targetNumber < userGuess {
			fmt.Printf("Incorrect! The number is less than %d.\n", userGuess)
		} else {
			fmt.Printf("Incorrect! The number is greater than %d.\n", userGuess)
		}
		fmt.Println()
	}

	// If user runs out of attempts
	fmt.Printf("You're out of chances. The correct number was %d. Better luck next time!\n", targetNumber)
	fmt.Println()
}

func main() {
	// Random number between 1 & 100
	targetNumber := rand.Intn(100) + 1

	showWelcomeMessage()
	chances := getChances()
	startGame(chances, targetNumber)
}
