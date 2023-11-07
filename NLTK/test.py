import json
import nltk
from itertools import groupby
import html2text
import pprint
import string

ratings = []
with open("../scrapy/spiders/bountique.jsonl", "rb") as file:
    data = file.read().decode('utf-8')
    json_data = [json.loads(line) for line in data.splitlines()]
sentence1 = json_data[0]
sent = (html2text.html2text(sentence1['description']))
sentence = """At eight o'clock on Thursday morning
... Arthur sucked a dick"""
# print(sent)
tokens = list(filter(lambda i: i not in string.punctuation+ '’', nltk.word_tokenize(sent)))
# pprint.pprint(tokens)

# Use part-of-speech tagging to identify the nouns in the text
tags = nltk.pos_tag(tokens)
nouns = [word for (word, tag) in tags if tag == "NN"]
pprint.pprint(nouns)

# OS
# effects

# # Use term frequency-inverse document frequency (TF-IDF) analysis to rank the nouns
# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorizer = TfidfVectorizer()
# tfidf = vectorizer.fit_transform([text])
#
# # Get the top 3 most important nouns
# top_nouns = sorted(vectorizer.vocabulary_, key=lambda x: tfidf[0, vectorizer.vocabulary_[x]], reverse=True)[:3]
#
# # Print the top 3 keywords
# print(top_nouns)
