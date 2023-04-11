import os
import speech_recognition as sp
import hotword
import importlib
import utils.speak
import config

def speech_recognizer():
	r = sp.Recognizer()
	#print(config.search_results)			
	with sp.Microphone() as source:
		print("Скажите что-нибудь")
		utils.speak.playlisten()
		#r.adjust_for_ambient_noise(source, duration=0.2)
		audio = r.listen(source)
		# print (config.searchindex)
		try:
			txt = r.recognize_google(audio, language="ru-RU")
			txt = txt.lower()
			print(txt)
			# plugins
			for moduleName in os.listdir(config.directoryPath + "/plugins"):
				command = importlib.import_module("plugins." + moduleName)
				if (command.execute(txt)): break
		except sp.UnknownValueError:
			print("Не расслышал фразу")
			pass
		except sp.RequestError as e:
			print("Ошибка; {0}".format(e))
			pass
		except Exception as e:
			print ("error")
			pass
	# waiting for new hot word command
	hotword.hotword_recognizer()
