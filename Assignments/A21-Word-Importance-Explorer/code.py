# Word Importance Explorer using TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample 5 documents
documents = [
    "Machine learning is amazing and powerful",
    "AI and machine learning are transforming the world",
    "Deep learning is a subset of machine learning",
    "Artificial intelligence includes machine learning",
    "Learning algorithms improve with data"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

# Display top words for each document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1}:")
    scores = zip(feature_names, doc.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    for word, score in sorted_scores[:3]:
        print(f"{word}: {score:.3f}")
