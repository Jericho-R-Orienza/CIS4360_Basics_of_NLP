"""
In this first task the directions are as follows:

Select a business b1 randomly from the dataset, then
extract all reviews for b1 to form a small dataset B1. Show word frequency
distributions in B1 before and after stemming, respectively. You may choose the
stemming algorithm implemented in any toolkit. You may consider plotting the
word frequency distributions in log-scale. Repeat the same process for another
randomly selected business b2. List the top-10 most frequent words (exclude
stopwords) before and after performing stemming, for each of the two selected
businesses. Stop words are the words that are commonly used but do not carry much
semantic meaning such as a, the, of, and.

"""

import json
# json is used to parse JSON files.

import random
# random is used to get random business

from collections import Counter
# Counter is a dict subclass for counting hashable objects. Here we use it to count words efficiently.

import re
# (Regular Expression) module is used for string searching and manipulation. Here, it's used to find words in the text.

import nltk
# (Natural Language Toolkit) is used for tokenization and stopword removal.

from nltk.stem.porter import PorterStemmer
# PorterStemmer is used for stemming, the process of reducing words to their word stem or root form.

from nltk.corpus import stopwords
# dict of stop words used to filter

# Ensure NLTK components are downloaded
nltk.download('punkt')  # for tokenization
nltk.download('stopwords')  # dictionary for stop words

#b1 and b2 holds the ID value while B1 and B2 will hold the data of the randomly selected IDs
def choose_two_random_business(data):
    b1 = random.choice(data)["business_id"]

    # Check we do not select a dupe for b2
    b2 = random.choice(data)["business_id"]
    while b2 == b1:
        b2 = random.choice(data)["business_id"]
    
    return b1, b2

def create_bussiness_ID_set(data, business_id):
    # Creating the data set for B1 and B2
    return [entry for entry in data if entry["business_id"] == business_id]

def get_top_10_words(B):
    # Get NLTK stop words
    stop_words = set(stopwords.words('english'))

    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()

    # Combine all text fields into one large string
    all_text = " ".join([entry["text"] for entry in B])

    # Tokenize and convert to lowercase, exclude stop words
    words = [word for word in re.findall(r'\b\w+\b', all_text.lower()) if word not in stop_words]

    # Count the non-stemmed words
    non_stemmed_word_count = Counter(words)

    # Stem the words and count again
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_word_count = Counter(stemmed_words)

    # Get the top 10 most common non-stemmed and stemmed words
    top_10_non_stemmed = non_stemmed_word_count.most_common(10)
    top_10_stemmed = stemmed_word_count.most_common(10)

    return top_10_non_stemmed, top_10_stemmed



file_path = 'reviewSelected100cleaned.json'

# Read and parse the JSON file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Randomly select two distinct Business IDs
b1, b2 = choose_two_random_business(data)

# Create datasets for the selected Business IDs
B1 = create_bussiness_ID_set(data, b1)
B2 = create_bussiness_ID_set(data, b2)

# Find the top 10 words (stemmed and non-stemmed) for each Business ID, excluding stop words
top_10_non_stemmed_b1, top_10_stemmed_b1 = get_top_10_words(B1)
top_10_non_stemmed_b2, top_10_stemmed_b2 = get_top_10_words(B2)

print(f"\nTop 10 non-stemmed words for Business 1 ID {b1}:")
for word, count in top_10_non_stemmed_b1:
    print(f"{word}: {count}")

print(f"\nTop 10 stemmed words for Business 1 ID {b1}:")
for word, count in top_10_stemmed_b1:
    print(f"{word}: {count}")

print(f"\nTop 10 non-stemmed words for Business 2 ID {b2}:")
for word, count in top_10_non_stemmed_b2:
    print(f"{word}: {count}")

print(f"\nTop 10 stemmed words for Business 2 ID {b2}:")
for word, count in top_10_stemmed_b2:
    print(f"{word}: {count}")



