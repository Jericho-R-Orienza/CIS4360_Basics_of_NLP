import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag_sents

# Ensure the necessary NLTK packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to load data from the JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

# Function to randomly select 5 entries and extract their text
def select_random_entries(data, count=5):
    selected_entries = random.sample(data, count)
    return [entry['text'] for entry in selected_entries]

# Function to apply the first POS tagging method
def pos_tag_texts_method1(texts):
    tagged_texts = []
    for text in texts:
        tokens = word_tokenize(text)
        tagged_texts.append(nltk.pos_tag(tokens))
    return tagged_texts

# Function to apply the second POS tagging method
def pos_tag_texts_method2(texts):
    tokenized_texts = [word_tokenize(text) for text in texts]
    tagged_texts = pos_tag_sents(tokenized_texts)
    return tagged_texts

# Load the data
data = load_data('reviewSelected100cleaned.json')  # Replace with your file path

# Select 5 random entries
random_texts = select_random_entries(data)

# Apply the first POS tagging method
tagged_texts_method1 = pos_tag_texts_method1(random_texts)

# Apply the second POS tagging method
tagged_texts_method2 = pos_tag_texts_method2(random_texts)

# Display the results for both methods
for i in range(len(random_texts)):
    print(f"Entry {i+1} with Method 1:")
    print(tagged_texts_method1[i])
    print(f"\nEntry {i+1} with Method 2:")
    print(tagged_texts_method2[i])
    print("\n")

