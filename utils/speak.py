from gtts import gTTS
from io import BytesIO
from tempfile import TemporaryFile
import time
import pyttsx3
from pathlib import Path
import utils.text
import config
from subprocess import Popen

from pydub import AudioSegment
from pydub.playback import play
from pydub import generators
from pydub.playback import _play_with_simpleaudio
import simpleaudio


def femaleVoice(text):
    print("Program : "+text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    try:
        print(text)
        tts = gTTS(text, lang=config.language)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        song = AudioSegment.from_file(fp, format="mp3")

        config.playback = _play_with_simpleaudio(song)
    except Exception:
        raise

def waitandspeak(text):
    try:
        tts = gTTS(text, lang=config.language)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        song = AudioSegment.from_file(fp, format="mp3")
        if (config.playback):
            config.playback.wait_done()
        config.playback = _play_with_simpleaudio(song)
    except Exception:
        raise

def speakchunks(text):
    print ("speak chunks")
    chunks = utils.text.splitText(text, 200)
    
    if len(chunks) > 1:
        print("2 chunks") 
        print("chunk 1: " + chunks[0])
        speak(chunks[0])
        print("chunk 2: " + chunks[1])        
        waitandspeak(chunks[1])        
    else:
        print ("1 chunk")
        speak(text)

def speakchunksmultiple(text):
    print ("speak chunks multiple")
    chunks = utils.text.splitTextMultiple(text, 300)
    if len(chunks) > 1: 
        print("chunk 1: " + chunks[0])
        speak(chunks[0])
        for index in range(1, len(chunks) - 1):
            print("chunk: " + chunks[index])        
            waitandspeak(chunks[index])        
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
