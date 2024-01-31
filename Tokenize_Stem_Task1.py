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
import random
from collections import Counter
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Ensure NLTK components are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def select_two_distinct_business_ids(data):
    b1 = random.choice(data)["business_id"]

    # Select b2 and ensure it's different from b1
    b2 = random.choice(data)["business_id"]
    while b2 == b1:
        b2 = random.choice(data)["business_id"]
    
    return b1, b2

def create_dataset_with_business_id(data, business_id):
    # Create a new dataset with entries having the specified Business ID
    return [entry for entry in data if entry["business_id"] == business_id]

def get_top_10_stemmed_words(B):
    # Get NLTK stop words
    stop_words = set(stopwords.words('english'))

    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()

    # Combine all text fields into one large string
    all_text = " ".join([entry["text"] for entry in B])

    # Tokenize and convert to lowercase, exclude stop words and stem
    words = [stemmer.stem(word) for word in re.findall(r'\b\w+\b', all_text.lower()) if word not in stop_words]

    # Count the words
    word_counts = Counter(words)

    # Get the top 10 most common stemmed words
    top_10 = word_counts.most_common(10)

    return top_10

# Replace 'your_file.json' with the path to your JSON file
file_path = 'reviewSelected100cleaned.json'

# Read and parse the JSON file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Randomly select two distinct Business IDs
b1_id, b2_id = select_two_distinct_business_ids(data)

# Create datasets for the selected Business IDs
B1 = create_dataset_with_business_id(data, b1_id)
B2 = create_dataset_with_business_id(data, b2_id)

# Find the top 10 stemmed words for each Business ID, excluding stop words
top_10_b1 = get_top_10_stemmed_words(B1)
top_10_b2 = get_top_10_stemmed_words(B2)

print(f"\nTop 10 stemmed words for Business ID {b1_id}:")
for word, count in top_10_b1:
    print(f"{word}: {count}")

print(f"\nTop 10 stemmed words for Business ID {b2_id}:")
for word, count in top_10_b2:
    print(f"{word}: {count}")


