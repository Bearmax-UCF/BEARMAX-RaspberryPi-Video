import requests
import os
from playsound import playsound

class AudioDisplay:
    def __init__(self, audioLink: str):
        self.audioLink = audioLink

    def audioDisplay(self):
        r = requests.get(self.audioLink)
        with open("audio.mp3", "wb") as f:
            f.write(r.content)

        file = "./audio.mp3"

        playsound(file, True)
        
        remove_downloaded_mp3(file)

def playAudioFunction(mediaURL: str):
    inputAudio = mediaURL
    audio = AudioDisplay(inputAudio)
    audio.audioDisplay()

def remove_downloaded_mp3(file_path: str):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print("MP3 file removed successfully:", file_path)
        else:
            print("File not found:", file_path)
    except Exception as e:
        print(e)
