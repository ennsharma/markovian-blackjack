import deck

class Table:

	def __init__(self, numPlayers):
		self.dealer = Dealer(self)
		self.players = [Player(i) for i in range(numPlayers)]

	def getPlayer(self, playerId):
		return self.players[playerId]

	def dealCard(self, playerId):
		print(self.dealer.dealCard(playerId))

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

	def computeHandValue(self):
		if self.hand:
			return sum([card.getNumericalValue() for card in self.hand])
		return 0

	def addCard(self, card):
		self.hand.append(card)

