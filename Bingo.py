import random
import math

class Bingo:
	def __init__(self):
		self.board = []

	def createBoard(self):
		for i in range(0,5):
			self.board.append([])
			for j in range(0,5):
				self.board[i].append([])

	def populateBoard(self):
		for i in range(0,len(self.board)):
			for j in range(0,len(self.board[i])):
				if i == 2 and j == 2:
					self.board[j][i] = "FREE"
				else:
					if i == 0:
						self.board[j][i] = random.randint(1,15)
					elif i == 1:
						self.board[j][i] = random.randint(16,30)
					elif i == 2 and (j != 2):
						self.board[j][i] = random.randint(31,45)
					elif i == 3:
						self.board[j][i] = random.randint(46,60)
					elif i == 4:
						self.board[j][i] = random.randint(61,75)

	def displayBoard(self):
		for k in range(0,len(self.board)):
			print(self.board[k])

	#@staticmethod
	def callSpace():
		numbers = []

		for k in range(75):
			numbers.append(k)

		data = []
		word = ['B','I','N','G','O']
		letterChosen = random.randint(0,len(word)-1)
		randomValue = random.choice(numbers)
		#randomValue = random.randint(15,85)
		numbers.remove(randomValue)
		data.append(letterChosen)
		data.append(randomValue)

		return data

	def markBoard(self,call):
		print(call[0],call[1])
		bingo = "BINGO"
		for i in range(0,len(self.board)):
			if(self.board[call[0]][i] == call[1]):
				self.board[call[0]][i] = "X"

		self.displayBoard()

	def oneBoardSimulation(self):
		#simulation for one board
		self.createBoard()
		self.populateBoard()
		self.displayBoard()

		for iteration in range(0,501):
			print(f"Call {iteration}:")
			print("\n")
			call = self.callSpace()
			self.markBoard(call)

	def checkRowsForBingo(self, row):
		spacesMarked = 0
		for i in range(len(self.board)):
			if self.board[row][i] == "X":
				spacesMarked += 1
		return spacesMarked == len(self.board)

	def checkColumnsForBingo(self, column):
		spacesMarked = 0
		for j in range(len(self.board)):
			if self.board[j][column] == "X":
				spacesMarked += 1
		return spacesMarked == len(self.board)

	def checkDiagonalsForBingo(self):
		left_to_right = 0
		right_to_left = 0

		for i in range(5):
			if self.board[i][i] == "X":
				left_to_right += 1

			if self.board[i][4 - i] == "X":
				right_to_left += 1

		return left_to_right == 5 and right_to_left == 5

	def cryBingo(self):
		for i in range(5):
			if self.checkRowsForBingo(i) or self.checkColumnsForBingo(i) or self.checkDiagonalsForBingo():
				return True
		return False

def main():
	#Question: How many turns would it take for someone to cry Bingo for n players?
	table = []
	numberOfPlayers = int(input("How many players for the game? "))
	simulations = int(input("How many simulations do you want to run? "))
	for i in range(0,numberOfPlayers):
		table.append(Bingo())
		table[i].createBoard()
		table[i].populateBoard()

	for j in range(0,simulations):
		print(f"Call {j}:")
		for k in range(0,len(table)):
			print(f"Player {k+1}:")
			playerJustGotBingo = False
			callOutSpace = Bingo.callSpace()
			table[k].markBoard(callOutSpace)

			if (table[k].cryBingo() is True):
				print(f"Player {k+1} got Bingo after {j+1} calls.")
				return

main()