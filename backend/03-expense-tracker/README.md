# Expense Tracker

A simple command-line interface (CLI) based Expense Tracker built with Go. This application allows you to manage your finances. The application allows you to add, delete, and view your expenses.

## Features

-   [x] Add an expense with a description and amount.
-   [] Update an expense.
-   [] Delete an expense.
-   [x] View all expenses.
-   [] View a summary of all expenses.
-   [] View a summary of expenses for a specific month (of current year).

## Sample Commands

```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10
```
