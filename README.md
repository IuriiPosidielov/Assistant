# Assistant

Linux version of Assistant (tested on Raspbery Pi)

sudo apt install portaudio19-dev

sudo apt install mpv

pip install pyaudio simpleaudio wikipedia openai pydub pyttsx3 gtts speechrecognition pvporcupine

Install youtube-dl:
download from github youtube-dl
sudo apt install pandoc
make
copy youtube-dl to /usr/bin

Autostart:
At the end of /home/pi/apps/.config/lxsession/LXDE-pi/autostart
put
@sh /home/pi/apps/Assistant/blue.sh                       # this line in case to activate bluetooth (if no bluetooth don't need)
@lxterminal -e python /home/pi/apps/Assistant/main.py     # start application in the terminal


blue.sh - contains id of bluetooth device (put your device)


