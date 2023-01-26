# import pandas as pd
# df=pd.read_excel("raildata.xlsx")
# from pydub import AudioSegment
# from gtts import gTTS
# import pygame
# def mergeAudios(audios):
#     combined = AudioSegment.empty()
#     for audio in audios:
#         combined += AudioSegment.from_mp3(audio)
#     return combined
# #
# #
# def mixedmusic(number1):
#     audios=[f"{number1}_Hindi.mp3",f"{number1}_English.mp3"]
#     announcement = mergeAudios(audios)
#     announcement.export(f"{number1}_mixedmusic.mp3", format="mp3")
#
# mixedmusic(df.Train[9])


from subprocess import call
class callpy(object):

    def __init__(self, path='C:\Users\DELL\PycharmProjects\pythonProject\audiotest.py'):
        self.path=path

    def call_python_file(self):
        # call(["Python3", "{}".format(self.path)])
        call(["Python3", "{}".format(self.path)])

if __name__ == "__main__":
    c=callpy()
    c.call_python_file()
