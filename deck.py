import itertools
import random

class Deck:

	suits = ['C', 'D', 'H', 'S']
	values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

	def __init__(self):
		self.cards = [Card(suit, value) for suit, value in itertools.product(self.suits, self.values)]
		self.shuffle()
		self.ctr = 0

	def drawCard(self):
		drawnCard = self.cards[self.ctr]
		self.ctr = self.ctr + 1
		return drawnCard

	def shuffle(self):
		random.shuffle(self.cards)
		self.ctr = 0


class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def getNumericalValue(self):
		if self.value in ['J', 'Q', 'K', 'A']:
			return 10 
		# TODO: Encode ace as 1 or 11
		return int(self.value)

	def __str__(self):
		return "%s%s" % (self.value, self.suit)
	