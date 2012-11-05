#-*- coding: utf-8 -*-
# Japanese Verb Practice Program - Bryan Becker - August 2012

import Verbs

def verbTest():
	index = 0
	while index < 5:
		Verbs.randomVerbFunc()
		index += 1
		continue
		contPrac = input("Do you want to continue practicing? Yes/No ")
		if contPrac == "Yes" or contPrac == "yes":
			index = 0
			continue
		elif contPrac == "No" or contPrac == "no":
			print("Alright, we can always pick up later.")
	optionChoice = input("What did you want to do now? Percentages/Practice/Exit ")
	if optionChoice == "Exit" or optionChoice == "exit":
		print("Alright, keep up the practice in the meantime! がんばってよ！")
	elif optionChoice == "Practice":
		verbTest()


name = input("Hi there! Welcome to the humble Nihongo Verb trainer! お名前は？ ")
print("Nice to meet you, {}!".format(name))
getStarted = input("Shall we get started? Yes/No ")
if getStarted == "Yes" or getStarted == "yes":
	verbTest();
elif getStarted == "No" or getStarted == "no":
	print("Alright, well I'll see you around sometime.")
	

