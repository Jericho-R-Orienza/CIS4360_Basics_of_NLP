"""
The directions for the third task are aas follows:

Each review has a “star” rating in the range of 1 to 5. Randomly select 50 reviews (one from each
business) of rating 1, extract the top-10 most frequent noun-adjective pairs from the
sentences in these selected reviews. Example noun-adjective pairs are service-
great, food-delicious, that appear in the same sentence. Do the same for 20 reviews
of ratings 2, 3, 4, and 5, respectively.
"""
import json
import random
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from itertools import product

# Ensure the necessary NLTK packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Function to load data from the JSON file
def read_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

# Function to randomly select reviews based on rating
def select_reviews_by_rating(data, rating, count):
    filtered_reviews = [d for d in data if d['stars'] == rating]
    selected_reviews = random.sample(filtered_reviews, min(count, len(filtered_reviews)))
    return [review['text'] for review in selected_reviews]

# Function to find noun-adjective pairs
def find_noun_adj_pairs(text):
    pairs = []
    stop_words = set(stopwords.words('english'))  # Set of English stop words
    for sentence in sent_tokenize(text):
        tokens = word_tokenize(sentence)
        # Filter out stop words and punctuation
        tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
        tagged = nltk.pos_tag(tokens)
        nouns = [word for word, pos in tagged if pos.startswith('NN')]
        adjs = [word for word, pos in tagged if pos.startswith('JJ')]

        # Create pairs from every combination of nouns and adjectives in the sentence
        pairs.extend(product(nouns, adjs))
    return pairs

# Load the data
data = read_file('reviewSelected100cleaned.json')  

# Process for each star rating
for rating in range(1, 6):
    count = 50 if rating == 1 else 20
    reviews = select_reviews_by_rating(data, rating, count)
    all_pairs = []

    for review in reviews:
        pairs = find_noun_adj_pairs(review)
        all_pairs.extend(pairs)

    # Count the frequency of each pair
    freq_pairs = Counter(all_pairs)
    top_10_pairs = freq_pairs.most_common(10)

    print(f"Top-10 noun-adjective pairs for {rating}-star reviews:")
    for pair, freq in top_10_pairs:
        print(f"{pair}: {freq}")
    print("\n")

