import random

val = [7, 8, 9, 10, 12, 13, 14, 11]
#col = [a, b, c, d]

handPl1 = []
handPl2 = []

value = ["7", "8", "9", "10", "Jack", "queen", "king", "Ace"]
colour = ["hearts", "diamonds", "spades", "clubs"]

all_cards = []
for h in colour:
    for i in value:
        all_cards.append(i + " of " + h)
#print(all_cards)

def deal_cards():
    deal_number = 7
    random.shuffle(all_cards)
    count = 0
    pl1 = []
    while(count < deal_number):
        pl1.append(all_cards.pop())
        count = count + 1
    return pl1

handPl1 = deal_cards()

print(handPl1)