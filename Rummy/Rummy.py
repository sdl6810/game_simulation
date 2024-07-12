import math
import random
from Card import Card
from Deck import Deck
import matplotlib.pyplot as plt
import numpy as np

#defined number of cards in gin rummy
def sevenCardValue(deckOfCards):
	random.shuffle(deckOfCards)
	faceCards = ['K','Q','J']
	numberCards = ['2','3','4','5','6','7','8','9','10']
	total = 0
	hand = []
	for i in range(0,8):
		hand.append(random.choice(deckOfCards))
		if hand[i]._rank == 'A':
			total = total + 1
		elif (hand[i]._rank in faceCards):
			total = total + 10
		elif (hand[i]._rank in numberCards):
			total = total + 5
	return total

def nthCardValues(numberOfCards,deckOfCards):
	d = Deck()
	random.shuffle(deckOfCards)
	faceCards = ['K','Q','J']
	numberCards = ['2','3','4','5','6','7','8','9','10']
	total = 0
	hand = []
	for i in range(0,numberOfCards):
		cardPicked = random.choice(deckOfCards)
		hand.append(cardPicked)
		d.removeCard(cardPicked)
		if hand[i]._rank == 'A':
			total = total + 1
		elif (hand[i]._rank in faceCards):
			total = total + 10
		elif (hand[i]._rank in numberCards):
			total = total + 5
	return total

#values is a list
def generateHistogram(values):
	dataRanges = [0,10,20,30,40,50]
	stemAndLeaf = [0,0,0,0,0,0]
	for j in range(0,len(values)):
		if (0 <= values[j] <= 10):
			stemAndLeaf[0] = stemAndLeaf[0]+1
		elif (11 <= values[j] <= 20):
			stemAndLeaf[1] = stemAndLeaf[1]+1
		elif (21 <= values[j] <= 30):
			stemAndLeaf[2] = stemAndLeaf[2]+1
		elif (31 <= values[j] <= 40):
			stemAndLeaf[3] = stemAndLeaf[3]+1
		elif (41 <= values[j] <= 50):
			stemAndLeaf[4] = stemAndLeaf[4]+1

	return stemAndLeaf

def main():
	d = Deck()
	# for i in range(0,len(d.cards)):
	# 	print(d.cards[i]._rank + " of " + d.cards[i]._suite)

	data = []
	intervals = [0,10,20,30,40,50]
	bins = range(0,51,5) #adjust the width here
	cardsDealt = 7

	j = 0
	while (j < 100000):
		data.append(nthCardValues(cardsDealt,d.cards))
		#print(f"Simulation {j+1}: {data[j]}")
		j = j + 1

	print(len(data))

	histogram = generateHistogram(data)
	print(['0-10','11-20','21-30','31-40','41-50'])
	print(histogram)
	plt.xlabel('Total Value')
	plt.ylabel('Frequency')
	plt.title(f'Histogram of {cardsDealt} Card Values')
	plt.xticks(bins)
	plt.hist(data,bins=bins,edgecolor='black')
	plt.grid(axis='y',alpha=0.75)
	plt.show()

main()