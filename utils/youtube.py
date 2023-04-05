import config
import config
from subprocess import Popen
from bs4 import BeautifulSoup
import re, requests, urllib.parse, urllib.request
from pygame import mixer
import utils.speak

def search(searchText):
    query_string = urllib.parse.urlencode({"search_query": searchText})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    config.search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    config.search_results = list(dict.fromkeys(config.search_results))
    config.searchindex = 0

def play_music(path):
	Popen("start /b " + "mpv//mpv.exe " + path + " --no-video --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt", shell=True)

def stop_music():
	Popen('taskkill /F /IM mpv.exe', shell=True)
	mixer.music.stop()
	
def openYouTube(search_results, index):
	Popen('taskkill /F /IM mpv.exe', shell=True)
	utils.speak.playok()
	youtubeLink = "https://www.youtube.com/watch?v={}".format(search_results[index])
	clip = requests.get(youtubeLink)
	clip2 = youtubeLink
	print(clip2)
	inspect = BeautifulSoup(clip.content, "html.parser")
	yt_title = inspect.find_all("meta", property="og:title")
	for concatMusic1 in yt_title:
		pass
	print(concatMusic1['content'])	
	print(clip2)
	play_music(clip2)