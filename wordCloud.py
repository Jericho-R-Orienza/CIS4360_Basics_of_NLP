import json
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to load data from the JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

# Function to randomly select three businesses and collect their reviews
def get_reviews_for_three_businesses(data):
    selected_businesses = random.sample(data, 3)
    reviews = {}
    for business in selected_businesses:
        business_id = business['business_id']
        if business_id not in reviews:
            reviews[business_id] = ''
        reviews[business_id] += business['text'] + ' '
    return reviews

# Function to generate a word cloud
def generate_word_cloud(text, title):
    wordcloud = WordCloud(width = 800, height = 800, 
                          background_color ='white', 
                          min_font_size = 10).generate(text)
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0)
    plt.title(title)
    plt.show()

# Load the data
data = load_data('reviewSelected100cleaned.json')  # Replace with your file path

# Get reviews for three businesses
business_reviews = get_reviews_for_three_businesses(data)

# Generate and display word clouds for each business
for business_id, reviews in business_reviews.items():
    generate_word_cloud(reviews, f'Word Cloud for Business ID: {business_id}')
