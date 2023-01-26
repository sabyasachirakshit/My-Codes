import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
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
    print(df)
    for index, item in df.iterrows():
        textToSpeech(item['Train'], '3_music.mp3')
        textToSpeech(item['Name'], '4_music.mp3')
        textToSpeech(item['From'], '6_music.mp3')
        textToSpeech(item['Via'], '8_music.mp3')
        textToSpeech(item['To'], '10_music.mp3')
        textToSpeech(item['Platform'], '12_music.mp3')

        audios = [f"{i}_music.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['Train']}.mp3", format="mp3")
if __name__ == "__main__":
    print("Now Generating Announcement...")
    generateAnnouncement("raildata.xlsx")