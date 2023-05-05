from gtts import gTTS
import utils.speak
#import plugins.zchatgpt
import plugins.kidpuzzle
import time
import os
import config
import tempfile
import simpleaudio as sa
import tempfile
import wave

#plugins.zchatgpt.execute ("расскажи сколько капель воды в стакане")
#plugins.zchatgpt.execute ("расскажи если объем стакана 200 мл")
#plugins.zchatgpt.execute ("расскажи если объем стакана 100 мл и крупная капля при комнатной температуре воздуха")

#как приготовить расскажи как приготовить салат оливье

#time.sleep(1)
#utils.speak.waitandspeak ("кто такие динозавры")
plugins.kidpuzzle.execute ("загадай загадку")

print(config.PuzzleAnswer)
plugins.kidpuzzle.execute (config.PuzzleAnswer)


time.sleep(10)
