import config
from subprocess import Popen
from bs4 import BeautifulSoup
import re, requests, urllib.parse, urllib.request
import utils.speak
import os

def search(searchText):
	try:
		query_string = urllib.parse.urlencode({"search_query": searchText})
		formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
		config.search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
		config.search_results = list(dict.fromkeys(config.search_results))
		config.searchindex = 0
	except Exception as e:
		pass

def play_music(path):
	try:
		print(path)
		Popen("/usr/bin/mpv " + path + " --no-video", shell=True)
	except Exception as e:
		pass

def stop_music():
	try:
		os.system("/usr/bin/killall mpv")
		if (config.playback):
			config.playback.stop()
		print("stop")
	except Exception as e:
		pass
	
def openYouTube(search_results, index):
	try:
		os.system("/usr/bin/killall mpv")
		utils.speak.playok()
		youtubeLink = "https://www.youtube.com/watch?v={}".format(search_results[index])
		play_music(youtubeLink)
	except Exception as e:
		pass

	
