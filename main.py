import os
import hotword
import time
import utils.speak
from subprocess import Popen

time.sleep(5)
p = Popen('echo "connect D4:F5:47:85:3A:C3" | bluetoothctl', shell=True)
time.sleep(1)
p.kill()

time.sleep(5)
utils.speak.playlisten()		
hotword.hotword_recognizer()
