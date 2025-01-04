

#auction program
auction_bids = {}
auction_active = True

while auction_active:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  auction_bids[name] = bid
  if input("Are there any other bidders? (y/n): ").lower() == "n":
    auction_active = False

#find highest bid
highest_bid = 0
winner = ""

#use max function to find highest bid
highest_bid = max(auction_bids.values())
winner = max(auction_bids, key=auction_bids.get)


#print the winner
print(f"The winner is {winner} with a bid of ${highest_bid}") 