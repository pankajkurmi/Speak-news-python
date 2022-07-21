from reprlib import aRepr
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=b07c825c19e9426cbddfd314bf185702"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    print(arts)
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")


