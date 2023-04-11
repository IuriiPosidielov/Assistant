from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
import time
import pyttsx3
from pathlib import Path
import config
import pydub
import io
from mpg123 import Mpg123, Out123
import os

def speak(text):
    try:
        tts = gTTS(text, lang='ru')
        sf = io.BytesIO()
        tts.write_to_fp(sf)
        sf.seek(0)
        mp3 = Mpg123()
        mp3.feed(sf.read())
        out = Out123()
        for frame in mp3.iter_frames(out.start):
            out.play(frame)
    except Exception:
        raise



speak ("Не расслышал фразу")
time.sleep(1)
os.system("/usr/bin/killall mpg123")
speak ("Не расслышал фразу Не расслышал фразу Не расслышал фразу Не расслышал фразу Не расслышал фразу Не расслышал фразу")
os.system("/usr/bin/killall mpg123")
speak ("Не расслышал фразу")


