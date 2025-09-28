from functools import reduce

# make main function to do everything
def main():
    expenses = {}

    while True: # create a loop to ask the question so long as the user keeps entering expenses
        name = input("Enter the type of expense (or 'done' to finish): ") # ask user for expense type
        # a way to break the loop
        if name.lower() == "done":
            break
        amount = float(input(f"Enter the amount for {name}: ")) # ask user for corresponding expense amount
        expenses[name] = amount

    if not expenses: # in case no input is entered
        print("No expenses entered.")
        return

    amounts = list(expenses.values())

    # calculate total amount, highest amount, and lowest amount
    total = reduce(lambda x, y: x + y, amounts)
    highest = reduce(lambda x, y: x if x > y else y, amounts)
    lowest = reduce(lambda x, y: x if x < y else y, amounts)

    # figures out the name of the highest and lowest expense
    highest_name = [name for name, amt in expenses.items() if amt == highest]
    lowest_name = [name for name, amt in expenses.items() if amt == lowest]

    # print for user to view
    print(f"Total expenses: ${total:.2f}")
    print(f"Highest expense(s): {highest_name} (${highest:.2f})")
    print(f"Lowest expense(s): {lowest_name} (${lowest:.2f})")

main()
