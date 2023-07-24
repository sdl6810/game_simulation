import math
from statistics import mode
from collections import Counter
from openpyxl import load_workbook, Workbook
import os, sys

class Card():
	def __init__(self,rank,suite):
		self._rank = rank
		self._suite = suite
		self.value = self.determineCardValue()

	def determineCardValue(self):
		if self._rank == 'A':
			self.value = 15
		elif self._rank == 10 or self._rank == 'J' or self._rank == 'Q' or self._rank == 'K':
			self.value = 10
		elif 2 <= self._rank <= 9:
			self.value = 5

	def getCardID(self):
		print(f"{self._rank} of {rank._suite}")

class cardDeck():
	def __init__(self):
		self.ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
		self.suites = ['Spades', 'Diamonds', 'Clubs', "Hearts"]
		self.deck = []
		for i in range(0,len(self.suites)-1):
			for j in range(0,len(self.ranks)):
				self.deck.append(Card(self.ranks[j],self.suites[i]))

	#algorithmically randomizes shuffle
	def basicRandomizedShuffle(self):
		return self.deck.shuffle

	def basicInterlaceShuffle(self):
		firstHalf = []
		secondHalf = []				
		for i in range(0,len(self.deck)-1):
			if i%2 == 0:
				firstHalf.append(self.deck[i])
			elif i%2 == 1:
				secondHalf.append(self.deck[i])

		j = len(firstHalf)-1
		while len(firstHalf) >= 0:
			secondHalf.append(firstHalf[j])
			firstHalf.remove(firstHalf[j])
			j = j - 1

#player strategies should go in this class as well
class CardPlayer():
	def __init__(self,name):
		self.score = 0
		self._name = name
		self.cardsInHand = []
		self.cardsOnBoard = []
		self.playedCards = []
		self.playerIn = True

	def computeTotalCardValues(self,cards):
		cardValues = 0
		for m in range(0,len(cards)):
			cardValues = cardValues + cards[m].value

		return cardValues

	def playerOut(self):
		if len(self.cardsInHand) == 0:
			self.playerStatus = False

	# def takeAction(self,boardCards,playerCards):
	# 	#player must choose from the following actions:
	# 	#pick a card from the deck
	# 	#take the following cards from discard pile up to and including the card desired
	# 	#if they take from the discard pile they MUST place a set or a run of at least three cards down
	# 	#they must discard a card from their hand
	# 	if boardCards == 0:
	# 		#if a player has a run
	# 		tempOfRanks = []
	# 		for i in range(0,len(playerCards)-1):
	# 			tempOfRanks.append(boardCards[i].rank)

	# 		modes = mode(tempOfRanks)


	# 		#if a player has a set
	# 	else:
	# 		continue
	# 	return None

class RummySim():
	def __init__(self,numberOfPlayers):
		self.table = []
		for i in range(0,numberOfPlayers):
			print(f"Enter player number {i}'s name: ")
			playerName = input()
			self.table.append(CardPlayer(playerName))

		self.deckOfCards = cardDeck()
		self.discardPile = []
		self.finalGameScores = []
		self.gameInProgress = True
		self.playerOutOfCards = False
		self.board = []

	def getPlayerIndex(self,nameOfPlayer):
		for k in range(0,len(self.table)-1):
			if self.table[k]._name == nameOfPlayer:
				break
			else:
				continue

		return k

	#assuming the first card is the top card
	def deal(self,numberOfCards,nameOfPlayer):
		i = 1
		playerInQuestion = self.getPlayerIndex(nameOfPlayer)
		while i <= len(self.table):
			self.table[playerInQuestion].cardsInHand.append(self.deckOfCards.deck[0])
			self.deckOfCards.deck.remove(0)
			i = i + 1

	#assuming the top is the first card
	def setupGame(self):
		i = 1
		while i <= len(self.table):
			print(type(self.deckOfCards.deck))
			self.deal(7,self.table[i].cardsInHand.append(self.deckOfCards.deck[0]))
			self.discardPile.append(self.deckOfCards.deck[0])
			self.deckOfCards.deck.remove(0)

	def recordGameFlowToXl(self,data,filepath):
		return None

	def writeScoresToXl(self,data,filepath):
		return None

	def play(self):
		while self.gameInProgress:
			self.setupGame()

			print("Game in progress.  Put in game code logic here.")

			i = 0
			#maybe consider designing this to be a linked list instead of just numerating and using modular arithmetic
			while not self.table[i].playerOut():
				print("Game is in progress")
				#develop game logic here
				#check again for any players who have gone out after their game

				#check if player is out
				if self.table[i].playerOut():
					#have players tabulate scores and then determine winner
					#store scores in a spreadsheet if desired.  Another round can be run if asked, otherwise game will exit
					for player in range(0, len(self.table)-1):
						if self.table[i].cardsInHand >= 1:
							#each card remaining in player's hand will be deducted from player's total score
							addUpCardsOnBoard = self.table[i].computeTotalCardValues(self.table[i].cardsInHand)*(-1)
						
						deductThoseInHand = self.table[i].computeTotalCardValues(self.table[i].cardsOnBoard)
						self.table[i].score = addUpCardsOnBoard - deductThoseInHand
						self.finalGameScores.append(self.table[i].score)

					winner = max(self.finalGameScores)
					print(f"Player {self.table[i]._name} is the winner of this round.")
					self.gameInProgress = False

				else:
					i = (i+1)%len(self.table)

def main():
	rummy = RummySim(4)
	rummy.play()

main()