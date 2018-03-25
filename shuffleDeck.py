import itertools, random
deck = list(itertools.product(range(1,14),['s','h','d','c']))
random.shuffle(deck)
botCards=[]
playerCards=[]
potCards=[]
potLabelIndicator=[0]*6
def distribute(numberOfCards, player):
	for i in range(numberOfCards):
		if(player==0):
			botCards.append(deck[0][1]+str(deck[0][0]))
			del(deck[0])
		elif(player==1):
			playerCards.append(deck[0][1]+str(deck[0][0]))
			del(deck[0])
		else:
			potCards.append(deck[0][1]+str(deck[0][0]))
			del(deck[0])

