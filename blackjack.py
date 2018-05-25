import deck

class Table:

	def __init__(self, numPlayers):
		self.dealer = Dealer(self)
		self.players = [Player(i) for i in range(numPlayers)]

	def getPlayer(self, playerId):
		return self.players[playerId]

	def dealCard(self, playerId):
		return self.dealer.dealCard(playerId)

class Dealer:
	
	def __init__(self, table):
		self.deck = deck.Deck()
		self.table = table

	def dealCard(self, playerId):
		card = self.deck.drawCard()
		self.table.players[playerId].addCard(card)
		return card

	def collectCards(self):
		self.deck.shuffle()

class Player:

	def __init__(self, playerId):
		self.hand = []
		self.id = playerId

	def getAceNum(self):
		count = 0
		for card in self.hand:
			if card.value == 'A':
				count += 1

		return count

	def computeHand(self, currHand, currValue):
		if len(currHand) == 0:
			return [currValue]
		card = currHand[0]
		remainHand = []
		if len(currHand) > 1:
			remainHand = currHand[1:]

		if card.value == 'A':
			a1 = self.computeHand(remainHand, currValue+card.getNumericalValue()[0])
			a11 = self.computeHand(remainHand, currValue+card.getNumericalValue()[1])

			vals = []
			for i in range(len(a1)):
				vals.append(a1[i])

			for j in range(len(a11)):
				vals.append(a11[j])

			return vals

		return self.computeHand(remainHand, currValue + card.getNumericalValue())
	

	def computeHandValue(self):
		return self.computeHand(self.hand, 0)

	def addCard(self, card):
		self.hand.append(card)

	def __str__(self):
		print_hand = []
		for card in self.hand:
			print_hand.append(card.value)
		return " ".join(print_hand)

