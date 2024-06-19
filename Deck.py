import random
import math
from Card import Card

class Deck:
	def __init__(self):
		self.cards = []
		self.ranks = []
		for i in range(0,13):
			if (i == 0):
				self.ranks.append('Ace')
			elif (1 <= i <= 10):
				self.ranks.append(str(i))
			elif (i == 11):
				self.ranks.append('Jack')
			elif (i == 12):
				self.ranks.append('Queen')
			elif (i == 13):
				self.ranks.append('King')

		self.suites = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

		self.newDeck()

	def newDeck(self):
		i = 0
		j = 0
		while i < 52:
			self.cards.append(Card(self.suites[i // 13], self.ranks[i % 13]))
			if (i % 13 == 0 and i != 0):
			    j = j + 1
			i = i + 1

	def removeCard(self,card):
		for c in self.cards:
			if c._suite == card._suite and c._rank == card._rank:
				self.cards.remove(c)
				break

	def dealACard(self):
		#pick card from the top of the pile
		cardDealt = self.cards[0]
		self.cards.remove(0)
		return cardDealt
