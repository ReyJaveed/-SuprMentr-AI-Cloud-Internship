# Simple Sentiment Analyzer

from textblob import TextBlob

reviews = [
    "This movie was amazing and fantastic!",
    "I hated this film, it was terrible",
    "It was okay, not great but not bad",
    "Absolutely loved the storyline",
    "Worst movie ever"
]

for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    print(f"\nReview: {review}")
    print(f"Sentiment: {sentiment}")
