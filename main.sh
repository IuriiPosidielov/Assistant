#!/bin/sh
killall lxterminal
killall xterm

sleep 5

xterm -hold -e /usr/bin/python3 /home/pi/apps/Assistant/mainkey.py &

exit
