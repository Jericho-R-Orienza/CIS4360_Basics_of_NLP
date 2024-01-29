import json

# Function to load data from the JSON file
def load_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
    return data

# Function to find the number of unique business IDs
def count_unique_business_ids(data):
    business_ids = set()
    for entry in data:
        business_ids.add(entry['business_id'])
    return len(business_ids)

# Load the data
data = load_data('reviewSelected100cleaned.json')  # Replace with your file path

# Count unique business IDs
unique_business_id_count = count_unique_business_ids(data)

# Print the result
print(f"Number of unique business IDs: {unique_business_id_count}")


