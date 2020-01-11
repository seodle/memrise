#!/usr/bin/env python
# coding: utf-8

from gtts import gTTS
import os

# Define the language

language = "en"

# import your word from a text file

myTextImport = open("memrise_words.txt", "r")

for line in myTextImport:

	print(line + " converting...")


	myText = line.replace("\n", "") #replace line breals by space

	# Create output

	output = gTTS(text = myText, lang = language, slow = False) #slow = False for normal speech rate

	# Export audio files

	output.save(myText+".mp3")

# Close the file
myTextImport.close()
