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

	def computeHand(self, currHand, currValue):
		if len(currHand) == 0 or currValue >= 22:
			return currValue
		card = currHand[0]
		remainHand = []
		if len(currHand) > 1:
			remainHand = currHand[1:]

		if card.value == 'A':
			a1 = self.computeHand(remainHand, currValue+card.getNumericalValue()[0])
			a11 = self.computeHand(remainHand, currValue+card.getNumericalValue()[1])

			hand1 = min(a1, 22)
			hand2 = min(a11, 22)

			if hand1 == 22 or hand2 == 22:
				return min(hand1, hand2)
			return max(hand1, hand2)

		return self.computeHand(remainHand, currValue + card.getNumericalValue())
	

	def computeHandValue(self):
		return self.computeHand(self.hand, 0)

	def addCard(self, card):
		self.hand.append(card)

