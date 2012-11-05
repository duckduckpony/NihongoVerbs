#-*- coding: utf-8 -*-
# Japanese Verb Practice Program - Bryan Becker - August 2012

import random

#Program needs to randomly pull verbs for user to guess, 
#so we establish the range of verbs, pull a random number,
#and then use that number to correlate to the verbNumber var of a specific verb via the verb dict
def randomVerbFunc():
	randVerbNum = random.randrange(1,len(verbNumbers) + 1)
	randVerb = verbNumbers[int(randVerbNum)]
	eval(randVerb).guessVerb()

class Verb(object):
	
	def __init__(self, verbName, verbClass, verbNumber, definitions, pronunciation):
		
		self.verbName = verbName
		
		# verbClass will divide verbs into sections depending on how common they are
		self.verbClass = verbClass
		
		# verbNumber will be placed in a dictionary that the program can randomly pull from
		self.verbNumber = verbNumber
		
		self.definitions = definitions
		
		self.pronunciation = pronunciation
		
		self.correctGuesses = 0
		
		self.incorrectGuesses = 0
		
	
	def guessVerb(self):
		verbAnswer = input("What does {} mean? ".format(self.verbName))
		if verbAnswer == self.definitions[0] or verbAnswer == self.definitions[1] or verbAnswer == self.definitions [2]:
			print("Correct! Good going!")
			self.correctGuesses += 1
			pronunAnswer = input("Now, what about the romaji? ")
			if pronunAnswer == self.pronunciation:
				print("Great! You got this verb down!")
			else:
				print("Good guess, but the pronunciation is actually {}.".format(self.pronunciation))
		else:
			print("Sorry, the correct answer is {}.".format(self.definitions[0]))
			self.incorrectGuesses += 1
	
	def calculatePercentage(self):
		correctPercentage = (self.correctGuesses / (self.correctGuesses + self.incorrectGuesses)) * 100


verbSuru = Verb("する", 1, 1, ["to do", "to make", "NULL"], "suru")
verbIku = Verb("行く", 1, 2, ["to go", "NULL", "NULL"], "iku")
verbTaberu = Verb("食べる", 1, 3, ["to eat", "to subsist", "NULL"], "taberu")
verbNomu = Verb("飲む", 1, 4, ["to drink", "to smoke", "to quaff"], "nomu")
verbKuru = Verb("来る", 1, 5, ["to come", "NULL", "NULL"], "kuru")
verbMiru = Verb("見る", 1, 6, ["to see", "to dream", "NULL"], "miru")
verbKaeru = Verb("かえる", 1, 7, ["to return", "NULL", "NULL"], "kaeru")
verbKiku = Verb("聞く", 1, 8, ["to listen", "to hear", "NULL"], "kiku")
verbAkeru = Verb("開ける", 1, 9, ["to open", "to become civilized", "NULL"], "akeru")
verbTatsu = Verb("立つ", 1, 10, ["to stand", "to rise", "to be excited"], "tatsu")


#assign verb name as a key to each verbNumber 
#so that randVerbFunc() can call it easily
verbNumbers = {
    verbSuru.verbNumber : "verbSuru",
    verbIku.verbNumber : "verbIku",
    verbTaberu.verbNumber : "verbTaberu",
    verbNomu.verbNumber : "verbNomu",
	verbKuru.verbNumber : "verbKuru",
	verbMiru.verbNumber : "verbMiru",
	verbKaeru.verbNumber : "verbKaeru",
	verbKiku.verbNumber : "verbKiku",
	verbAkeru.verbNumber : "verbAkeru",
	verbTatsu.verbNumber : "verbTatsu"
}




