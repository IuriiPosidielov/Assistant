from gtts import gTTS
from io import BytesIO
import time
from pydub import AudioSegment
from pydub.playback import play

from pydub import generators
from pydub.playback import _play_with_simpleaudio

import simpleaudio

tts = gTTS("кто такие динозавры", lang='ru')

fp = BytesIO()
tts.write_to_fp(fp)
fp.seek(0)

song = AudioSegment.from_file(fp, format="mp3")
#play(song)
#print ("hel")
#time.sleep(10)


# 5 seconds of A 440
#sound = generators.Sine(440).to_audio_segment(duration=5000)

##### using pydub's helper function:
playback = _play_with_simpleaudio(song)

# end playback after 3 seconds
print("hello")
time.sleep(1)
print("simple")
playback.wait_done()
#playback.stop()

##### using simpleaudio directly:
playback = simpleaudio.play_buffer(
    song.raw_data, 
    num_channels=song.channels, 
    bytes_per_sample=song.sample_width, 
    sample_rate=song.frame_rate
)
# end playback after 3 seconds
print("simple")
time.sleep(1)
print("simple")

playback.stop()
