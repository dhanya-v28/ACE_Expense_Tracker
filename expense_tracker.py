# Expense Tracker

# Stores all recorded expenses
expenses = []

while True:
    # Display main menu
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    # -------------------- Add Expense --------------------
    if choice == "1":

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        category = input("Enter category: ")
        description = input("Enter description: ")

        # Store one expense as a dictionary
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        # Add the expense to the list
        expenses.append(expense)

        print("Expense added successfully!")

    # -------------------- View Expenses --------------------
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n========== ALL EXPENSES ==========")

            # Used to number each expense
            expense_num = 1

            # Display each recorded expense
            for expense in expenses:
                print(
                    "Expense", expense_num,
                    "| Amount:", expense["amount"],
                    "| Category:", expense["category"],
                    "| Description:", expense["description"]
                )

                expense_num += 1

    # -------------------- Show Summary --------------------
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            category_totals = {}

            # Calculate total and category-wise spending
            for expense in expenses:
                amount = expense["amount"]
                category = expense["category"]

                total += amount

                # Create a category if it does not already exist
                if category not in category_totals:
                    category_totals[category] = 0

                # Add the expense amount to its category total
                category_totals[category] += amount

            # Display total spending
            print("\n========== EXPENSE SUMMARY ==========")
            print("Total amount spent:", total)

            # Display spending for each category
            print("\nAmount spent in each category:")
            for category, amount in category_totals.items():
                print(category, ":", amount)

            # Find the category with the highest spending
            highest_category = max(
                category_totals,
                key=category_totals.get
            )

            print("\nHighest spending category:", highest_category)
            print("Amount spent:", category_totals[highest_category])

    # -------------------- Exit --------------------
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")