# Text Challenges - Preprocessing Example

import re
import string

# Sample 20 messy sentences
sentences = [
    "OMG 😱 I luv this!!!",
    "Ths is gr8, totally awesome 😎",
    "idk what 2 do :(",
    "LOL 😂 that's hilarious",
    "Cant wait 4 the party!!!",
    "I rly like this movie, it's amazng",
    "U shud try this, super fun!!",
    "Wowwwww 😍 so coool",
    "btw, thx 4 ur help",
    "Hmmmm 🤔 not sure about it",
    "Plz send it asap",
    "Gr8 job 👏",
    "smh, I can't believe it",
    "R u coming 2nite?",
    "This is soooo boring 😴",
    "lmao 😂 that was epic",
    "Thx a lot!",
    "Haven't seen u in ages 😢",
    "Y u so serious?",
    "Can't wait 4 nxt episode!"
]

# Preprocessing: lowercase, remove punctuation, remove emojis (simple)
cleaned_sentences = []
for sent in sentences:
    # lowercase
    sent = sent.lower()
    # remove emojis (keep simple by removing non-ascii)
    sent = sent.encode('ascii', 'ignore').decode('ascii')
    # remove punctuation
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    cleaned_sentences.append(sent)

print("Original Sentences:\n", sentences)
print("\nCleaned Sentences:\n", cleaned_sentences)
