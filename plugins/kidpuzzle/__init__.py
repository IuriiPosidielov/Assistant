import utils.fuzzy
import utils.speak
import utils.text
import config
import sqlite3
import random
import os

def get_rnd_puzzle():
	id = random.randint(1,1342)
	path = os.path.abspath(__file__)
	dir_path = os.path.dirname(path)
	print(dir_path)
	con = sqlite3.connect(dir_path + "/main.db")
	cur = con.cursor()
	cur.execute('select Question,Answer from Puzzle where ID=(?)',(id,))
	res=cur.fetchone()
	con.close()
	return res[0],res[1]

def execute(text):
	print(text)
	hotword_first = utils.fuzzy.includeWord(["загадай загадку"], text)
	if hotword_first:
		puzzle,answer = get_rnd_puzzle()
		print(puzzle)
		print(answer)
		config.PuzzleAnswer = answer.lower()
		utils.speak.speakwithcaching(puzzle)
		return True

	hotword_second = utils.fuzzy.includeWord([config.PuzzleAnswer], text)
	if hotword_second:
		print("Correct answer:" + config.PuzzleAnswer)
		utils.speak.speak("Урааа!!! Супер! Молодец! " + config.PuzzleAnswer + " это правильный ответ!")
		return True
	return False
