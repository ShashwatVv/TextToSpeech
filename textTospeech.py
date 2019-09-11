#google text to speech API
#Author : Shashwat Vaibhav
from gtts import gTTS
import os

Mtext = "Hello there, Shashwat!"

language = "en"

output = gTTS(text=Mtext, lang = language, slow = False)

output.save("Music.mp3")

os.system("start Music.mp3")
