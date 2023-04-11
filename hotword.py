import os
import struct
import pyaudio
import pvporcupine
import speech 
import config


# print(pvporcupine.KEYWORDS)
def hotword_recognizer():
    porcupine = None
    pa = None
    audio_stream = None

    try:
        access_key = config.hotword_access_key

        handle = pvporcupine.create(access_key=access_key, keywords=config.hotword_keywords)

        pa = pyaudio.PyAudio()
        frame = 512

        audio_stream = pa.open(
                        rate=16000,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=frame)
        print("please say hot word:")
        while True:
            pcm = audio_stream.read(frame)
            pcm = struct.unpack_from("h" * frame, pcm)
            keyword_index = handle.process(pcm)

            if keyword_index >= 0:
                print("Hotword Detected")
                speech.speech_recognizer()
    finally:
        print("finally")
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.stop_stream()
            audio_stream.close()

        if pa is not None:
                pa.terminate()