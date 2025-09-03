# Function 1 will keep track of the tickets sold
def purchases(tickets_left):
    # prompt user for number of tickets they'd like to buy
    num = int(input("Welcome to the Cinema Ticket Pre-Sale! Please enter tickets to buy; up to 4 tickets per buyer: "))
    # make sure no buyer purchases more than 4 or the remaining number of tickets
    if 1 <= num <= 4 and num <= tickets_left:
        # return the number of tickets to buy
        return num
    else:
        # in the event a user enters a number more than 4 or if tickets remaining is insufficient to complete request
        print("Invalid number of tickets.\n")
        return 0

# Function 2 displays the remaining tickets
def show_remain(tickets_left):
    # print how many tickets are left after each purchase
    print(f"Available tickets remaining: {tickets_left}\n")


# main program
def main():
    # initialize variables, starting with 20 tickets and no buyers
    tickets_left = 20
    buyers = 0

    # continue selling tickets until all purchased, and update the number of buyers after each purchase
    while tickets_left > 0:
        purchased = purchases(tickets_left)
        if purchased > 0:
            tickets_left -= purchased
            buyers += 1
            #show how many tickets are left
            show_remain(tickets_left)

    # print statement and buyer tally once all tickets are sold
    print(f"All tickets sold! Total buyers: {buyers}")
    print('Bye')

# start program by calling main
main()

