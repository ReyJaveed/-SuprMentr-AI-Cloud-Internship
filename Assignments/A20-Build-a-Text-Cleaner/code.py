# Build a Text Cleaner

import string
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Sample messy sentences
sentences = [
    "OMG 😱 I luv this!!!",
    "Ths is gr8, totally awesome 😎",
    "idk what 2 do :(",
    "LOL 😂 that's hilarious",
]

# Define stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Clean all sentences
cleaned_sentences = [clean_text(sent) for sent in sentences]

print("Original Sentences:\n", sentences)
print("\nCleaned Sentences:\n", cleaned_sentences)
