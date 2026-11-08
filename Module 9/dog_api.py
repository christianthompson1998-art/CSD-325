
import requests

# Connect to the Dog API
url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

# Test the connection
print("Status Code:", response.status_code)

# Print the original response
print("\nUnformatted Response:")
print(response.text)

# Print the formatted response
print("\nFormatted Response:")

if response.status_code == 200:
    data = response.json()

    print("Dog Image:", data["message"])
    print("Status:", data["status"])
else:
    print("API connection failed.")
