"""
Requests module providing access to API's.
We will use it to access currency exchange data.
"""

import requests

# Ask user for currency information
from_currency = input("Enter from currency: ").upper().strip()
to_currency = input("Enter to currency: ").upper().strip()
amount = float(input("Enter amount: "))

# Enter your API key here (if needed )
API_KEY = "122a76de7e1339ad9a91fb11"

# Generate the URL you will be requesting (read the documentation on the API site)
URL = f"https://open.er-api.com/v6/latest/{from_currency}"

# Use Requests to get data from the URL back in JSON format
# JSON = javascript object notation (you can also use XML but I prefer JSON)
json_data = requests.get(URL, timeout=10).json()

# Use brackets just like in lists and dictionaries to get the exact data you need
# Use a JSON viewer like https://codebeautify.org/jsonviewer to read your JSON
rate = json_data['rates'][to_currency]

# Convert currency
converted = amount * rate

# Print the conversion
print("Currency Exchange")
print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")