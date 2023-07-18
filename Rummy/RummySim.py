import math
from openpyxl import load_workbook, Workbook
import os, sys

class Card(rank,suite):
	def __init__(self,rank,suite):
		self._rank = rank
		self._suite = suite
		self.value = determineCardValue()

	def determineCardValue(self):
		if 2 <= self._rank <= 9:
			self.value = 5
		elif self._rank == 'A':
			self.value = 15:
		elif self._rank == 10 or self._rank == 'J' or self._rank == 'Q' or self._rank == 'K':
			self.value = 10

class cardDeck():
	def __init__(self):
		self.ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
		self.suites = ['Spades', 'Diamonds', 'Clubs', "Hearts"]
		self.deck = []
		for i in range(0,len(self.suites)-1):
			deck.append(Card(self.suites[i]))
			for j in range(0,len(self.ranks)):
				self.deck[i].ranks = self.ranks[j]

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
class CardPlayer(name):
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

	def takeAction():
		#player must choose from the following actions:
		#pick a card from the deck
		#take the following cards from discard pile up to and including the card desired
		#if they take from the discard pile they MUST place a set or a run of at least three cards down
		#they must discard a card from their hand

class RummySim():
	def __init__(self,numberOfPlayers):
		self.table = []
		for i in range(0,numberOfPlayers):
			print(f"Enter player number {i}'s name: ")
			playerName = input()
			self.table.append(CardPlayer(playerName))
		setupGame()

		self.deck = cardDeck()
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
		playerInQuestion = getPlayerIndex(nameofPlayer)
		while i <= numberOfCards:
			self.table[playerInQuestion].append(self.deck[0])
			self.deck.remove(0)
			i = i + 1

	#assuming the top is the first card
	def setupGame(self):
		i = 1
		while i <= playersInRound:
			deal(7,self.table[i].cardsInHand.append(self.deck[0]))
			self.discardPile.append(self.deck[0])
			self.deck.remove(0)

	def writeToXl(data,filepath):
		return None

	def checkForOuts(self):
		p = 0
		while p <= len(self.table):
			if self.table[p].playerOut == True
				self.playerOutOfCards = True

	def play():
		while self.gameInProgess:
			#develop game logic here
			print("Game is in progress")

			#check again for any players who have gone out after their game
			checkFourOuts()
			if !checkForOuts():
				#have players tabulate scores and then determine winner
				#store scores in a spreadsheet if desired.  Another round can be run if asked, otherwise game will exit
				for player in range(0, len(self.table)-1):
					if self.table[i].cardsInHand >= 1:
						#each card remaining in player's hand will be deducted from player's total score
						x = self.table[i].computeTotalCardValues(self.table[i].cardsInHand)*(-1)
					
					y = self.table[i].computeTotalCardValues(self.table[i].cardsOnBoard)
					self.table[i].score = x + y
					self.finalGameScores.append(self.table[i].score)

				winner = max(self.finalGameScores)
				print(f"Player {self.table[i]._name} is the winner of this round.")
				self.gameInProgress = False