"""
todo: In this program, our objective is to make a program in python that will read us the latest news headlines.
"""
import requests


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=8a652cc67fc743da8ce6a1d36dd2756c')
response = requests.get(url)
response1 = response.json()
j = 1
for i in response1["articles"]:
    str1 = (i["title"])
    print(f"Number {j} news is ")
    print(str1)
    speak(f"Number {j} news is")
    speak(str1)
    j += 1
print('\nHit Enter to End.......')
input()
