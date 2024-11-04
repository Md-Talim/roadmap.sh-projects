package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"time"
)

var fileName = "expenses.json"

type Expense struct {
	ID          int       `json:"id"`
	Description string    `json:"description"`
	Amount      float64   `json:"amount"`
	Date        time.Time `json:"date"`
}

func loadExpenses() []Expense {
	var emptyExpense []Expense
	file, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Println("Error opening file: ", err)
		return emptyExpense
	}

	var expenses []Expense
	err = json.Unmarshal(file, &expenses)
	if err != nil {
		fmt.Println("Error unmarshalling JSON:", err)
		return emptyExpense
	}

	return expenses
}

func saveExpenses(expenses []byte) {
	err := os.WriteFile(fileName, expenses, 0644)

	if err != nil {
		fmt.Println("Error writing to JSON file:", err)
		return
	}
}

func addExpense(description string, amount float64) {
	expenses := loadExpenses()

	id := expenses[len(expenses)-1].ID + 1
	newExpense := Expense{id, description, amount, time.Now()}

	expenses = append(expenses, newExpense)
	updatedData, err := json.MarshalIndent(expenses, "", "    ")
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}

	saveExpenses(updatedData)
	fmt.Printf("Expense added successfully (ID: %d)\n", id)
}

func listExpenses() {
	expenses := loadExpenses()

	if len(expenses) == 0 {
		fmt.Println("There are no entries.")
		return
	}

	fmt.Printf("%-3s %-15s %-20s %s\n", "ID", "Date", "Description", "Amount")
	for _, expense := range expenses {
		fmt.Printf("%-3d %-15s %-20s $%.2f\n", expense.ID, expense.Date.Format("2006-01-02"), expense.Description, expense.Amount)
	}
}

func deleteExpense(id int) {
	if id == -1 {
		fmt.Println("Please enter the ID of the extpense to delete.")
		return
	}

	expenses := loadExpenses()

	if len(expenses) == 0 {
		fmt.Println("There are no entries.")
		return
	}

	expenseIndex := -1
	for index, expense := range expenses {
		if expense.ID == id {
			expenseIndex = index
		}
	}

	if expenseIndex == -1 {
		fmt.Printf("Expense with ID: %d not found!", id)
		return
	}

	expenses = append(expenses[:expenseIndex], expenses[expenseIndex+1:]...)

	updatedExpenses, err := json.MarshalIndent(expenses, "", "    ")
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}

	saveExpenses(updatedExpenses)
	fmt.Printf("Expense with ID: %d deleted!\n", id)
}

type SummaryOptions struct {
	Month int
}

var MONTHS = []string{"", "January", "February", "March", "April", "May", "June", "July", "August", "Semptember", "October", "November", "December"}

func showSummary(options *SummaryOptions) {
	expenses := loadExpenses()
	totalExpense := 0.0

	if options.Month == -1 {
		for _, expense := range expenses {
			totalExpense += expense.Amount
		}

		fmt.Printf("Total expenses: $%.0f\n", totalExpense)
	} else {
		currentTime := time.Now()
		currentYear, _, _ := currentTime.Date()

		for _, expense := range expenses {
			year, month, _ := expense.Date.Date()

			if year == currentYear && MONTHS[options.Month] == month.String() {
				totalExpense += expense.Amount
			}
		}

		fmt.Printf("Total expenses for %s: $%.0f\n", MONTHS[options.Month], totalExpense)
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Invalid format!")
		os.Exit(1)
	}

	action := os.Args[1]

	switch action {
	case "add":
		addCmd := flag.NewFlagSet("add", flag.ExitOnError)
		description := addCmd.String("description", "", "Description of the transaction")
		amount := addCmd.Float64("amount", 0.0, "Amount for the transaction.")

		addCmd.Parse(os.Args[2:])

		addExpense(*description, *amount)
	case "list":
		listExpenses()
	case "delete":
		deleteCmd := flag.NewFlagSet("delete", flag.ExitOnError)
		id := deleteCmd.Int("id", -1, "ID of the expense to delete")
		deleteCmd.Parse(os.Args[2:])
		deleteExpense(*id)
	case "summary":
		summaryCmd := flag.NewFlagSet("summary", flag.ExitOnError)
		month := summaryCmd.Int("month", -1, "Name of the month.")
		summaryCmd.Parse(os.Args[2:])
		showSummary(&SummaryOptions{Month: *month})
	default:
		fmt.Println("Enter a valid action!")
	}
}
