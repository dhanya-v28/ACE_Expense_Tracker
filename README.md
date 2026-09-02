# Expense Tracker

A simple **command-line Expense Tracker** built using Python. It allows users to record expenses and view useful spending summaries.

## Features

* Add an expense with amount, category, and description
* View all recorded expenses
* Calculate total amount spent
* Calculate category-wise spending
* Find the highest-spending category
* Handle invalid amount input and invalid menu choices

## Approach

Expenses are stored in a **list**. Each expense is represented using a **dictionary** containing its amount, category, and description.

A `while` loop keeps the menu running until the user chooses to exit.

A `for` loop is used to display expenses and process them for the summary. A separate dictionary called `category_totals` stores the total amount spent in each category.

The `max()` function is used to find the category with the highest spending.

## Concepts Used

* Variables
* Input/Output
* Conditions
* `while` and `for` loops
* Lists
* Dictionaries
* `try-except`
* `max()`

## How to Run

Make sure Python is installed.

Open the terminal in the project folder and run:

```bash
python expense_tracker.py
```
## Note

This is a command-line based project developed as part of the college Technical Society task of Programming Domain.