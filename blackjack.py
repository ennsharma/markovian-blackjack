import deck

class Table:
	def __init__(self, numPlayers):
		self.dealer = Dealer()
		self.players = [Player() for i in range(numPlayers)]

class Dealer:
	def __init__(self):
		self.deck = deck.Deck()

	def dealCard(self, playerID):
		return # TODO

	def collectCards(self):
		self.deck.shuffle()

class Player:

	def __init__(self):
		self.hand = []

	def computeHandValue(self):
		return # TODO

	def hitMe(self):
		return # TODO

