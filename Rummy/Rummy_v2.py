import math
import random
from Card import Card
from Deck import Deck

faceCards = ['K','Q','J','A']
numberCards = ['2','3','4','5','6','7','8','9','10']

class Rummy_v2():
	def __init__(self):
		self.deck = Deck()
		self.discardPile = []
		self.table = []
		self.playerOut = False
		self.gameOver = False

	def setupGame(self,players):
		for i in range(0,players):
			self.table.append(RummyPlayer())

	def distributeCards(self,numberOfCards):
		#random.shuffle(self.deck.cards)
		for a in range(0,len(self.table)):
			for c in range(1,numberOfCards):
				cardOffTopOfPile = self.deck.cards[0]
				self.table[a].holdingCards.append(cardOffTopOfPile)
				self.deck.removeCard(cardOffTopOfPile)

	def assignNumericaValues(cards):
		cardRankings = []

		for card in cards:
			if card._rank == "A":
				cardRankings.append(1)
			elif card._rank in numberCards:
				cardRankings.append(int(card._rank))
			elif card._rank == 'J':
				cardRankings.append(11)
			elif card._rank == 'Q':
				cardRankings.append(12)
			elif card._rank == 'K':
				cardRankings.append(13)

		return cardRankings

	@staticmethod
	def hasSameRanks(cards):
		ranks = Rummy_v2.assignNumericaValues(cards)
		ranks.sort()

		count = 1

		for i in range(1,len(ranks)):
			if abs(ranks[i-1] - ranks[i]) == 0:
				count +=1
				if count == 3:
					return True
			else:
				count = 1

		return False

	@staticmethod
	def countSuites(cards,suite):
		suiteCount = 0
		#diamonds, clubs, hearts, spades
		for card in cards:
			if card._suite == suite:
				suiteCount += 1

		return suiteCount

	@staticmethod
	def hasConsecutiveRanks(cards):
		ranks = Rummy_v2.assignNumericaValues(cards)
		ranks.sort()

		rank_set = set(ranks)  # Convert ranks to a set for quick lookup
		min_rank = min(ranks)  # Get the minimum rank in the sorted list
		max_rank = max(ranks)  # Get the maximum rank in the sorted list

		for rank in range(min_rank, max_rank - 1):
			if rank in rank_set and rank + 1 in rank_set and rank + 2 in rank_set:
				return True

		return False

	@staticmethod
	def hasAStraightFlush(cards,suiteInQuestion):
		ranks = Rummy_v2.assignNumericaValues(cards)
		suiteCount = Rummy_v2.countSuites(cards,suiteInQuestion)
		
		if suiteCount < 3:
			return False
		
		ranks.sort()
		
		count = 1
		straight_flush = False

		for i in range(1,len(ranks)):
			if ranks[i] == ranks[i-1] + 1:
				count +=1
				if count >= 3:
					straight_flush = True
			elif ranks[i] != ranks[i-1]:
				count = 1

		return False

	@staticmethod
	def areAPair(firstSecond):
		if first._rank == second._rank:
			return True
		else:
			return False

	@staticmethod
	def isThreeOfAKind(pair,thirdCard):
		firstTwo = areAPair(pair[0],pair[1])
		allThreeEqual = False
		if firstTwo:
			allThreeEqual = areAPair(pair[1],thirdCard)
			return True
		else:
			return False

	@staticmethod
	def areQuads(pair,anotherPair):
		firstPair = areAPair(pair[0],pair[1])
		secondPair = areAPair(anotherPair[0],anotherPair[1])
		if firstPair and secondPair and (pair[0]._rank == anotherPair._rank[0]):
			return True
		else:
			return False

	def runGameSimulation():
		while (self.gameOver is False):
			pass

class RummyPlayer():
	#the strategy of the player is two fold:
	#minimize the number of cards if not completely get rid of all their cards
	#maximize their number of points using the cards they played during the game

	def __init__(self):
		self.holdingCards = []
		self.score = 0
		self.wonGame = False
		self.cardsPlayed = []
		self.game = Rummy_v2()

	def calculateTotalScore(self):
		total = 0
		holdingCards = []
		for i in range(0,len(self.holdingCards)):
			if self.holdingCards[i]._rank == 'A':
				total = total + 1
			elif (self.holdingCards[i]._rank in faceCards):
				total = total + 10
			elif (self.holdingCards[i]._rank in numberCards):
				total = total + 5
		return total

def main():
	d = Deck()
	g = Rummy_v2()
	g.setupGame(2)
	random.shuffle(g.deck.cards)
	g.distributeCards(10)

	for player_idx in range(1,len(g.table)):
		print(f"Player {player_idx} cards:")
		for card in g.table[player_idx].holdingCards:
			print(f"{card._rank} of {card._suite}")

		diamondRunDetected = Rummy_v2.countSuites(g.table[player_idx].holdingCards,"Diamonds")
		heartsRunDetected = Rummy_v2.countSuites(g.table[player_idx].holdingCards,"Hearts")
		spadesRunDetected = Rummy_v2.countSuites(g.table[player_idx].holdingCards,"Spades")
		clubsRunDetected = Rummy_v2.countSuites(g.table[player_idx].holdingCards,"Clubs")

		print(f"Player {player_idx} - Number of diamonds in hand: {diamondRunDetected}")
		print(f"Player {player_idx} - Number of hearts in hand: {heartsRunDetected}")
		print(f"Player {player_idx} - Number of clubs in hand: {clubsRunDetected}")
		print(f"Player {player_idx} - Number of spades in hand: {spadesRunDetected}")

		straightDetected = Rummy_v2.hasConsecutiveRanks(g.table[player_idx].holdingCards)
		diamondFlush = Rummy_v2.hasAStraightFlush(g.table[player_idx].holdingCards,"Diamonds")
		heartFlush = Rummy_v2.hasAStraightFlush(g.table[player_idx].holdingCards,"Hearts")
		spadesFlush = Rummy_v2.hasAStraightFlush(g.table[player_idx].holdingCards,"Spades")
		clubFlush = Rummy_v2.hasAStraightFlush(g.table[player_idx].holdingCards,"Clubs")
		print(f"Striaght detected for Player {player_idx}: {straightDetected}")
		print(f"Straight flush detected for Player {player_idx} : {diamondFlush}")
		print(f"Straight flush detected for Player {player_idx} : {heartFlush}")
		print(f"Straight flush detected for Player {player_idx} : {clubFlush}")
		print(f"Straight flush detected for Player {player_idx} : {spadesFlush}")

main()