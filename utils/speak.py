from gtts import gTTS
import time
import pyttsx3
from pathlib import Path
import utils.text
import config
from mpg123 import Mpg123, Out123
from io import BytesIO
from subprocess import Popen
import os
import psutil

def femaleVoice(text):
    print("Program : "+text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    try:	
        tts = gTTS(text, lang=config.language)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        mp3 = Mpg123()
        mp3.feed(fp.read())
        out = Out123()
        for frame in mp3.iter_frames(out.start):
            out.play(frame)
    except Exception:
        raise

def speakchunks(text):
    print ("speak chunks")
    chunks = utils.text.splitText(text, 200)
    
    if len(chunks) > 1: 
        print("chunk 1: " + chunks[0])
        speak(chunks[0])
        print("chunk 2: " + chunks[1])        
        speak(chunks[1])        
    else:
        speak(text)

def speakchunksmultiple(text):
    print ("speak chunks multiple")
    chunks = utils.text.splitTextMultiple(text, 200)
    if len(chunks) > 1: 
        print("chunk 1: " + chunks[0])
        speak(chunks[0])
        for index in range(1, len(chunks) - 1):
            print("chunk: " + chunks[index])        
            speak(chunks[index])        
    else:
        speak(text)

def saveandspeak(text, path):
    try:
        path = path.replace(".txt", ".mp3")
        if Path(path).is_file():
            print ("wavfile" + path)
            play(path)
            return
        playthinking()
        tts = gTTS(text, lang=config.language)
        tts.save(tts.save(path))
        play(path)
    except Exception:
        raise

def speakwithcaching(content):
    print(content)
    if (len(content) < 200):
        print("less 200")
        speak(content)
        return
    if (len(content) > 2000):
        print("more 2000")
        utils.speak.speakchunksmultiple(content)
        return
    else:
        print ("more 200 and less 2000")
        utils.speak.speakchunks(content)


def play(file):
    Popen("/usr/bin/mpv " + file + " --no-video", shell=True)

def playok():
    play(config.directoryPath + "/sound/ok.mp3")

def playlisten():
    play(config.directoryPath + "/sound/listen.mp3")

def playthinking():
    play(config.directoryPath + "/sound/thinking.mp3")

def waitMpgRunning():
    try:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if 'mpg123' in proc.info['name']:
                return true
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return false
    return false

def waitandspeak(text):
    try:
        tts = gTTS(text, lang=config.language)
        sf = BytesIO()
        tts.write_to_fp(sf)
        sf.seek(0)
        mp3 = Mpg123()
        mp3.feed(sf.read())
        out = Out123()
        for frame in mp3.iter_frames(out.start):
            out.play(frame)
    except Exception:
        raise
