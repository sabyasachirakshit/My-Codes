import requests
def speak(str):
 from win32com.client import Dispatch
 speak=Dispatch("SAPI.SpVoice")
 speak.Speak(str)
url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=xxxxxxxxUseYourOwnApiKeyxxxxxxx')
response = requests.get(url)
response1=response.json()
j=1
for i in response1["articles"]:
    str1=(i["title"])
    print(f"Number {j} news is ")
    print(str1)
    speak(f"Number {j} news is")
    speak(str1)
    j+=1



