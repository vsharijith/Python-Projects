logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("Welcome to Secret Bidding Program!")

bids = {}

bid_continue = True


def find_highest_bidder(dictionary):
    winner = ''
    highest_bid = 0

    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")


while bid_continue is True:
    name = input("What is your name?\n")
    price = int(input("What is your Bid?\n$ "))
    bids[name] = price
    to_continue = input("Are there any other bids? Type 'yes' or 'no'.\n").lower()
    if to_continue == "no":
        bid_continue = False
        find_highest_bidder(bids)
    elif to_continue == "yes":
        print("\n"*50)
