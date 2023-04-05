#from googletrans import Translator
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
import time
import pyttsx3
from pathlib import Path
import utils.text
import config

def femaleVoice(text):
    print("Program : "+text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    try:
        #translator = Translator()
        # text=translator.translate(text, dest=lang).text
        tts = gTTS(text, lang=config.language)
        mixer.init()
        sf = TemporaryFile()
        tts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()
        #while mixer.music.get_busy():
        #   time.sleep(1)
    except Exception:
        raise

def speakchunks(text):
    print ("speak chunks")
    chunks = utils.text.splitText(text, 200)
    
    if len(chunks) > 1: 
        print("chunk 1: " + chunks[0])
        speak(chunks[0])
        print("chunk 2: " + chunks[1])        
        waitandspeak(chunks[1])        
    else:
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
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def playok():
    play("sound/ok.mp3")

def playlisten():
    play("sound/listen.mp3")

def playthinking():
    play("sound/thinking.mp3")

def waitandspeak(text):
    try:
        tts = gTTS(text, lang=config.language)
        sf = TemporaryFile()
        tts.write_to_fp(sf)
        sf.seek(0)
        while mixer.music.get_busy():
           time.sleep(1)
        print("play")
        play(sf)
    except Exception:
        raise
