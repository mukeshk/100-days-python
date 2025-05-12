import gavel_art
are_there_more_bidder = True
bids = {}
print(gavel_art.gavel)
while are_there_more_bidder:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount? :$"))
    bids[bidder_name]=bid_amount

    bidder_present = input("Are there more bidders present Type 'Yes' or 'No' ").lower()
    if bidder_present == 'no':
        are_there_more_bidder = False

max_bidder_amount = 0
winning_bidder = ""
for bidder in bids:
    if max_bidder_amount < bids[bidder]:
        winning_bidder = bidder
        max_bidder_amount = bids[bidder]

print(f"The winner of the bids is {winning_bidder} with bid amount ${max_bidder_amount}")


