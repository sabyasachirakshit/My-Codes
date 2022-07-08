import sys
import pandas as pd
from threading import Thread
from pydub import AudioSegment
from gtts import gTTS
import pygame
df=pd.read_excel("raildata.xlsx")
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    for index, item in df.iterrows():
        textToSpeech(item['Train'], '3_music.mp3')
        textToSpeech(item['Name'], '4_music.mp3')
        textToSpeech(item['From'], '6_music.mp3')
        textToSpeech(item['Via'], '8_music.mp3')
        textToSpeech(item['To'], '10_music.mp3')
        textToSpeech(item['Platform'], '12_music.mp3')

        audios = [f"{i}_music.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['Train']}_English.mp3", format="mp3")

def textToSpeech2(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
def generateAnnouncement2(filename):
    df = pd.read_excel(filename)
    for index, item in df.iterrows():
        textToSpeech2(item['From'], '2_hindi.mp3')
        textToSpeech2(item['Via'], '4_hindi.mp3')
        textToSpeech2(item['To'], '6_hindi.mp3')
        textToSpeech2(item['Train'], '8_hindi.mp3')
        textToSpeech2(item['Name'], '9_hindi.mp3')
        textToSpeech2(item['Platform'], '11_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['Train']}_Hindi.mp3", format="mp3")
if __name__ == "__main__":
    print("Now Generating Announcement...")
    generateAnnouncement("C:\\Users\\PC\\My Codes\\majorproject\\raildata.xlsx")
    generateAnnouncement2("C:\\Users\\PC\\My Codes\\majorproject\\raildata.xlsx")
