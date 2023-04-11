from subprocess import Popen
import time

time.sleep(5)
p = Popen('echo "connect D4:F5:47:85:3A:C3" | bluetoothctl', shell=True)
time.sleep(1)
p.kill()
