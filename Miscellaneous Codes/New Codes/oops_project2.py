from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import time


class Extraction:
    def __init__(self, text_str):
        self.text_str = text_str

    def Frequency_Table(self) -> dict:
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(self.text_str)
        ps = PorterStemmer()
        freqTable = dict()
        for word in words:
            word = ps.stem(word)
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        return freqTable

    def _score_sentences(self, sentences, freqTable) -> dict:
        sentenceValue = dict()
        for sentence in sentences:
            word_count_in_sentence_except_stop_words = 0
            for wordValue in freqTable:
                if wordValue in sentence.lower():
                    word_count_in_sentence_except_stop_words += 1
                    if sentence[:10] in sentenceValue:
                        sentenceValue[sentence[:10]] += freqTable[wordValue]
                    else:
                        sentenceValue[sentence[:10]] = freqTable[wordValue]

            if sentence[:10] in sentenceValue:
                sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]
                                                             ] / word_count_in_sentence_except_stop_words
        return sentenceValue

    def _find_average_score(self, sentenceValue) -> int:
        sumValues = 0
        for entry in sentenceValue:
            sumValues += sentenceValue[entry]
        average = (sumValues / len(sentenceValue))
        return average

    def _generate_info(self, sentences, sentenceValue, threshold):
        sentence_count = 0
        summary = ''
        for sentence in sentences:
            if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
                summary += " " + sentence
                sentence_count += 1
        return summary

    def launch_execution(self):
        freq_table = self.Frequency_Table()
        sentences = sent_tokenize(self.text_str)
        sentence_scores = self._score_sentences(sentences, freq_table)
        threshold = self._find_average_score(sentence_scores)
        information = self._generate_info(
            sentences, sentence_scores, 1.3 * threshold)
        return information


class Mining:  
    def __init__(self, text):
        self.text = text

    def Sentence_Tokenize(self):
        """Seperating all the sentences by tokenizing using in-built function."""
        tokenized_text = sent_tokenize(self.text)
        print(
            f"\n\nThe sentences after {self.Sentence_Tokenize.__doc__} from the given text :\n{tokenized_text}")

    def Word_Tokenize(self):
        """Seperating all the words by tokenizing using in-built function."""
        tokenized_word = word_tokenize(self.text)
        print(
            f"\n\nWords after {self.Word_Tokenize.__doc__} from the given text :\n{tokenized_word}")
        return tokenized_word

    def Purification(self):
        """Stopwords considered as noise in the text. Text may contain stop words such as is, am, are, this, a, an, the, etc.
            In NLTK for removing stopwords, you need to create a list of stopwords and filter out your list of tokens from these words."""
        tokenized_word = self.Word_Tokenize()
        purified_sentence = []
        stop_words = set(stopwords.words("english"))
        for w in tokenized_word:
            if w not in stop_words:
                purified_sentence.append(w)
        print("Tokenized Sentence with stopwords:", tokenized_word)
        print("Filtered Sentence without stopwords:", purified_sentence)
        return purified_sentence

    def Stemmer(self):
        """Stemming is a process of linguistic normalization, which reduces words to their word root word or chops off the derivational affixes.
    For example, connection, connected, connecting word reduce to a common word "connect"."""
        ps = PorterStemmer()
        stemmed_words = []
        filtered_sent = self.Purification()
        for w in filtered_sent:
            stemmed_words.append(ps.stem(w))
        print("Filtered Sentence:", filtered_sent)
        print("Stemmed Sentence:", stemmed_words)

    def Lemmatizer(self):
        """Lemmatization reduces words to their base word, which is linguistically correct lemmas. It transforms root word with the use of vocabulary and morphological analysis. Lemmatization is usually more sophisticated than stemming. Stemmer works on an individual word without knowledge of the context. For example, The word "better" has "good" as its lemma. This thing will miss by stemming because it requires a dictionary look-up."""
        words = self.Word_Tokenize()
        lem = WordNetLemmatizer()
        stem = PorterStemmer()
        for w in words:
            print(f"Lemmatized Word for {w} is {lem.lemmatize(w)}\n")
            print(f"Stemmed Word of {w} is {stem.stem(w)}")
            print("\n\n")


if __name__ == "__main__":
    print("1.Implementing Text Mining on Sample \n2.Extraction Of Meaningful Data from sample text\n")
    choice = int(input("Please Enter Your Choie(1-2): "))
    if choice == 1:
        print("Implementing Text mining on Sample Data.\n We will give a sample text as input and then we will do mining and extract tokenized sentences, tokenized words, stopwords, stem the words and lemmatize it.")
        text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
        The sky is pinkish-blue. You shouldn't eat cardboard. Indeed after hardship comes ease. After the dark clouds and the rain, comes the bright beautiful sunshine."""
        time.sleep(3)
        print(f"\n\nThe sample text that we will use is  given below:\n{text}")
        token_flow = Mining(text)
        time.sleep(3)
        token_flow.Sentence_Tokenize()
        time.sleep(2)
        token_flow.Word_Tokenize()
        time.sleep(2)
        print(
            f"\n\nNow, to filter the sentences by removing stopwords.\n{token_flow.Purification.__doc__}")
        token_flow.Purification()
        time.sleep(2)
        print(f"\nStemming---->\n{token_flow.Stemmer.__doc__}")
        token_flow.Stemmer()
        time.sleep(2)
        print(f"\nLemmatization---->{token_flow.Lemmatizer.__doc__}")
        token_flow.Lemmatizer()
    elif choice == 2:
        choice = int(
            input("1.Input Article\n2.Use Sample Article for testing purpose.\nEnter Choice(1-2): "))
        if choice == 2:
            text = ''' 
    Those Who Are Resilient Stay In The Game Longer
    “On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow.” — Friedrich Nietzsche
    Challenges and setbacks are not meant to defeat you, but promote you. However, I realise after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don’t have the answers. I can’t tell you what the right course of action is; only you will know. However, it’s important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it’s an opportunity to improve and find new ways to overcome their obstacles. Same failure, yet different responses. Who is right and who is wrong? Neither. Each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner means to succeed.
    I’ve coached mummy and mom clients who gave up after many years toiling away at their respective goal or dream. It was at that point their biggest breakthrough came. Perhaps all those years of perseverance finally paid off. It was the 19th Century’s minister Henry Ward Beecher who once said: “One’s best success comes after their greatest disappointments.” No one knows what the future holds, so your only guide is whether you can endure repeated defeats and disappointments and still pursue your dream. Consider the advice from the American academic and psychologist Angela Duckworth who writes in Grit: The Power of Passion and Perseverance: “Many of us, it seems, quit what we start far too early and far too often. Even more than the effort a gritty person puts in on a single day, what matters is that they wake up the next day, and the next, ready to get on that treadmill and keep going.”
    I know one thing for certain: don’t settle for less than what you’re capable of, but strive for something bigger. Some of you reading this might identify with this message because it resonates with you on a deeper level. For others, at the end of their tether the message might be nothing more than a trivial pep talk. What I wish to convey irrespective of where you are in your journey is: NEVER settle for less. If you settle for less, you will receive less than you deserve and convince yourself you are justified to receive it.
    “Two people on a precipice over Yosemite Valley” by Nathan Shipps on Unsplash
    Develop A Powerful Vision Of What You Want
    “Your problem is to bridge the gap which exists between where you are now and the goal you intend to reach.” — Earl Nightingale
    I recall a passage my father often used growing up in 1990s: “Don’t tell me your problems unless you’ve spent weeks trying to solve them yourself.” That advice has echoed in my mind for decades and became my motivator. Don’t leave it to other people or outside circumstances to motivate you because you will be let down every time. It must come from within you. Gnaw away at your problems until you solve them or find a solution. Problems are not stop signs, they are advising you that more work is required to overcome them. Most times, problems help you gain a skill or develop the resources to succeed later. So embrace your challenges and develop the grit to push past them instead of retreat in resignation. Where are you settling in your life right now? Could you be you playing for bigger stakes than you are? Are you willing to play bigger even if it means repeated failures and setbacks? You should ask yourself these questions to decide whether you’re willing to put yourself on the line or settle for less. And that’s fine if you’re content to receive less, as long as you’re not regretful later.
    If you have not achieved the success you deserve and are considering giving up, will you regret it in a few years or decades from now? Only you can answer that, but you should carve out time to discover your motivation for pursuing your goals. It’s a fact, if you don’t know what you want you’ll get what life hands you and it may not be in your best interest, affirms author Larry Weidel: “Winners know that if you don’t figure out what you want, you’ll get whatever life hands you.” The key is to develop a powerful vision of what you want and hold that image in your mind. Nurture it daily and give it life by taking purposeful action towards it.
    Vision + desire + dedication + patience + daily action leads to astonishing success. Are you willing to commit to this way of life or jump ship at the first sign of failure? I’m amused when I read questions written by millennials on Quora who ask how they can become rich and famous or the next Elon Musk. Success is a fickle and long game with highs and lows. Similarly, there are no assurances even if you’re an overnight sensation, to sustain it for long, particularly if you don’t have the mental and emotional means to endure it. This means you must rely on the one true constant in your favour: your personal development. The more you grow, the more you gain in terms of financial resources, status, success — simple. If you leave it to outside conditions to dictate your circumstances, you are rolling the dice on your future.
    So become intentional on what you want out of life. Commit to it. Nurture your dreams. Focus on your development and if you want to give up, know what’s involved before you take the plunge. Because I assure you, someone out there right now is working harder than you, reading more books, sleeping less and sacrificing all they have to realise their dreams and it may contest with yours. Don’t leave your dreams to chance.
    '''
            print(f"Sample Article is given below:\n{text}")
            Extractor = Extraction(text)
            print("Useful Short Info gained-->\n")
            print(Extractor.launch_execution())
        elif choice == 1:
            user_input_string = input("Enter Article:")
            Extractor = Extraction(user_input_string)
            print(Extractor.launch_execution())
        else:
            print("Wrong Choice!")
    else:
        print("Wrong Choice!")