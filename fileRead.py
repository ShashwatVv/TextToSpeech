#google text to speech API
#Author : Shashwat Vaibhav

from gtts import gTTS
import os

MyFile = open('SomeFile.txt', 'r') #create a file with any name(eg. SomeFile.txt)
                                   #and open it in read mode
MText = MyFile.read().replace("\n", " ")#replace end of line character

language = "en"

output = gTTS(text=Mtext, lang = language, slow = False)

output.save("Music.mp3")

os.system("start Music.mp3")
