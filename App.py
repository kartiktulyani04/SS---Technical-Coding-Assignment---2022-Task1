import requests

# Fetch JSON data from the API
api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Sort the data by descending popularity
    sorted_data = sorted(data, key=lambda x: x['Popularity'], reverse=True)

    # Display the data in the desired format
    for product in sorted_data:
        print(f"Title: {product['Title']}")
        print(f"Price: {product['Price']}")
        print(f"Popularity: {product['Popularity']}")
        print(f"Subcategory: {product['Subcategory']}")
        print("-" * 30)

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
import requests

# Fetch JSON data from the API
api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Sort the data by descending popularity
    sorted_data = sorted(data, key=lambda x: x['Popularity'], reverse=True)

    # Display the data in the desired format
    for product in sorted_data:
        print(f"Title: {product['Title']}")
        print(f"Price: {product['Price']}")
        print(f"Popularity: {product['Popularity']}")
        print(f"Subcategory: {product['Subcategory']}")
        print("-" * 30)

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
