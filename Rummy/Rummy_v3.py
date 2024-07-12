import math
import random
from Card import Card
from Deck import Deck
import openpyxl
from openpyxl import Workbook, load_workbook

faceCards = ['King','Queen','Jack','Ace']
numberCards = ['2','3','4','5','6','7','8','9','10']

class Rummy_v3():
	def __init__(self):
		self.deck = Deck()
		self.discardPile = []
		self.table = []
		self.runs = []
		self.matchedSuits = []
		self.playerOut = False
		self.gameOver = False

	def setupGame(self,players):
		for i in range(0,players):
			self.table.append(RummyPlayer())

	def distributeCards(self, numberOfCards):
		for a in range(len(self.table)):  # Iterate over each player in self.table
			for c in range(numberOfCards):  # Deal exactly numberOfCards cards to each player
				cardOffTopOfPile = self.deck.cards[0]
				self.table[a].holdingCards.append(cardOffTopOfPile)
				self.deck.removeCard(cardOffTopOfPile)

	def assignNumericaValues(self,cards):
		cardRankings = []

		for card in cards:
			if card._rank == "Ace":
				cardRankings.append(1)
				#Ace should be 1 not 14
			elif card._rank == "Jack":
				cardRankings.append(11)
			elif card._rank == "Queen":
				cardRankings.append(12)
			elif card._rank == "King":
				cardRankings.append(13)
			elif card._rank in numberCards:
				cardRankings.append(int(card._rank))
			else:
				print(f"Unknown card rank: {card._rank}")

		return cardRankings

	def hasSameRanks(cards):
		ranks = Rummy_v2.assignNumericaValues(cards)
		ranks.sort()

		count = 1

		for i in range(1,len(ranks)):
			if abs(ranks[i-1] - ranks[i]) == 0:
				count +=1
				if count >= 3:
					return True
			else:
				count = 1

		return False

	def haveSameSuite(self,cards,suite):
		suiteCount = 0
		#diamonds, clubs, hearts, spades
		for card in cards:
			if card._suite == suite:
				suiteCount += 1

		if suiteCount < 3:
			return False
		elif suiteCount >= 3:
			return True

		#return suiteCount

	def completeArithmeticSum(self,cards):
		ranks = self.assignNumericaValues(cards)
		ranks.sort()
		if len(ranks) < 2:
			return 0
		else:
			missingTerms = self.findMissingNumbers(ranks)
			n = len(ranks + missingTerms)

			return (n/2)*(ranks[0]+ranks[len(ranks)-1])

	def currentSumOfCards(self,cards):
		ranks = self.assignNumericaValues(cards)
		ranks.sort()
		s = 0
		for i in range(len(ranks)):
			s = s + ranks[i]

		return s

	def findMissingNumbers(self,ranks):
	    missingTerms = []
	    for i in range(len(ranks) - 1):
	        diff = ranks[i + 1] - ranks[i]
	        if diff > 1:
	            for j in range(1, diff):
	                missingTerms.append(ranks[i] + j)
	    
	    return missingTerms

	def cardsAreConsecutive(self,cards,suite):
		#formula based off arithmetic sequence formula for integers
		#(n/2)*(a[0] + a[n])
		certainSuitedCards = self.collectCardsWithSuite(cards,suite)
		ranksOfSuites = self.assignNumericaValues(certainSuitedCards)
		ranksOfSuites.sort()
		completeSum = self.completeArithmeticSum(certainSuitedCards)
		sumOfCards = self.currentSumOfCards(certainSuitedCards)

		if len(certainSuitedCards) < 3: 
			return False
		elif sumOfCards != completeSum:
			return False
		else:
			return True

	def collectCardsWithSuite(self,cards,suite):
		cardsWithSuite = []
		count = 1

		for card in cards:
			if card._suite == suite:
				cardsWithSuite.append(card)

		return cardsWithSuite

	def straightFlushExists(self,cards,suite):
		cardsWithSuite = self.collectCardsWithSuite(cards,suite)
		
		for i in range(0,len(cardsWithSuite)):
			print(f"{cardsWithSuite[i-1]._rank} of {cardsWithSuite[i-1]._suite}")
		numberOfCards = len(cardsWithSuite)
		completeSum = self.completeArithmeticSum(cardsWithSuite)

		thereIsAFlush = self.haveSameSuite(cardsWithSuite,suite)
		haveSameRank = self.cardsAreConsecutive(cardsWithSuite,suite)

		if thereIsAFlush and haveSameRank:
			cardSum = 0
			ranks = self.assignNumericaValues(cardsWithSuite)
			i = 0
			for card in cardsWithSuite:
				cardSum = cardSum + ranks[i]
				i +=1

			return True
		else:
			return False

	def identifyMissingCards(self,cards,suite):
		cardsWithSuite = self.collectCardsWithSuite(cards,suite)
		thereIsAFlush = self.straightFlushExists(cards,suite)
		completeSum = self.completeArithmeticSum(cardsWithSuite)
		ranks = self.assignNumericaValues(cardsWithSuite)
		ranks.sort()
		missingCards = []
		count = 1

		#if there are three cards of the same suite but it is not a flush, find the missing cards that will make it so
		tempSum = 0
		startFromIndex = 0
		tempIndex = 0
		m = 0
		while tempSum <= completeSum:
			if cards[startFromIndex]._rank + m not in ranks:
				missing.append(cards[startFromIndex]._rank + m)
				tempSum = tempSum + cards[m]._rank+1
			elif cards[startFromIndex]._rank + m in ranks:
				temp = m
				startIndex = temp
				m = 0
			m+=1

		return missing

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
		self.cardsInCommunity = []
		self.game = Rummy_v3()

	def calculateTotalScore(self):
		total = 0
		for i in range(0,len(self.holdingCards)):
			if self.holdingCards[i]._rank == 'A':
				total = total + 1
			elif (self.holdingCards[i]._rank in faceCards):
				total = total + 10
			elif (self.holdingCards[i]._rank in numberCards):
				total = total + 5
		return total

def main():
	g = Rummy_v3()
	g.setupGame(5)
	random.shuffle(g.deck.cards)
	g.distributeCards(7)

	for player_idx in range(0, len(g.table)):
		print(f"Player {player_idx} cards:")
		player_cards = g.table[player_idx].holdingCards
		for card in g.table[player_idx].holdingCards:
			print(f"{card._rank} of {card._suite}")
		# Check for straight flushes
		if g.cardsAreConsecutive(player_cards, "Diamonds"):
			print(f"Player {player_idx} has a straight flush in diamonds.")
		if g.cardsAreConsecutive(player_cards, "Hearts"):
			print(f"Player {player_idx} has a straight flush in hearts.")
		if g.cardsAreConsecutive(player_cards, "Spades"):
			print(f"Player {player_idx} has a straight flush in spades.")
		if g.cardsAreConsecutive(player_cards, "Clubs"):
			print(f"Player {player_idx} has a straight flush in clubs.")
		print("")

if __name__ == "__main__":
    main()