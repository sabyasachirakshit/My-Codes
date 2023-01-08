#translator in python
#easy coding :))

from tabulate import tabulate
from googletrans import Translator

class TranslatorClass(object):
    def __init__(self,word,lang):
        self.word = word
        self.lang = lang
        self.Trans = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translated = self.Trans.translate(self.word,dest=self.lang).text
        data = [
        ['Language:',"Word/sentence"],
        ['English', self.word],
        ['Arabic', str(translated)]]
        table = str(tabulate(data, headers="firstrow", fmt="grid"))
        return table


if __name__ == "__main__":
    translate = input('Enter word/sentence: ')
    language = 'ar'
    print(TranslatorClass(translate, language))


