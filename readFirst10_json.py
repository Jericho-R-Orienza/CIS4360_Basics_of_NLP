import json
import random

file_path = 'reviewSelected100cleaned.json'

def create_dataset_with_same_business_id(file_path):
    # Read and parse the JSON file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Randomly select one entry and get its Business ID
    random_entry = random.choice(data)
    selected_business_id = random_entry["business_id"]

    # Create a new dataset with entries having the same Business ID
    B1 = [entry for entry in data if entry["business_id"] == selected_business_id]

    return B1, selected_business_id

# Replace 'your_file.json' with the path to your JSON file
file_path = 'reviewSelected100cleaned.json'

# Create the dataset and retrieve the selected Business ID
B1, selected_business_id = create_dataset_with_same_business_id(file_path)
print(f"Selected Business ID: {selected_business_id}")
print(f"Number of entries in B1: {len(B1)}")

"""

# Read and parse the JSON file
with open(file_path, 'r', encoding = 'utf-8') as file:
    data = json.load(file)



# Iterate over the first ten entries
for entry in data[:10]:  # Assuming the data is a list of entries
    print("Review ID:", entry["review_id"])
    print("User ID:", entry["user_id"])
    print("Business ID:", entry["business_id"])
    print("Stars:", entry["stars"])
    print("Useful:", entry["useful"])
    print("Funny:", entry["funny"])
    print("Cool:", entry["cool"])
    print("Text:", entry["text"])
    print("Date:", entry["date"])
    print("-" * 30)  # Separator for readability

    random_entry = random.choice(data)
    print(random_entry)
"""

