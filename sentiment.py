import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
nltk.download('subjectivity')
nltk.download('movie_review')
analyzer = SentimentIntensityAnalyzer()
while True:
    next_message = input('message: ')
    scores = analyzer.polarity_scores(next_message)
    compound = scores['compound']
    if compound >0.1:
        print('it is a positive comment!')
    elif compound <0.1:
        print('it is negative comment!')
    else:
        print('it is a neutral comment!')