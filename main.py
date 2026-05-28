"""
Requests module providing access to API's.
We will use it to access currency exchange data.
and  it gives a joke at the end
"""

import requests

while True:

    # Ask user for currency information
    from_currency = input("Enter from currency: ").upper().strip()
    to_currency = input("Enter to currency: ").upper().strip()
    amount = float(input("Enter amount: "))

    # Enter your API key here (if needed )
    API_KEY = "122a76de7e1339ad9a91fb11"

    # Generate the URL you will be requesting (read the documentation on the API site)
    URL = f"https://v6.exchangerate-api.com/v6/122a76de7e1339ad9a91fb11/latest/{from_currency}"

    # Use Requests to get data from the URL back in JSON format
    # JSON = javascript object notation (you can also use XML but I prefer JSON)
    json_data = requests.get(URL, timeout=10).json()

    # Use brackets just like in lists and dictionaries to get the exact data you need
    # Use a JSON viewer like https:/ho/codebeautify.org/jsonviewer to read your JSON
    rate = json_data['conversion_rates'][to_currency]

    # Convert currency
    converted = amount * rate

    # Print the conversion
    print("Currency Exchange")
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    
    ########################################################################################

   # Joke APi hahaha 🤣🤣



    joke = input("\nDo you want to hear a joke? (y/n): ").lower().strip()

    if joke == "y":

        URL = "https://official-joke-api.appspot.com/random_joke"

        json_data = requests.get(URL, timeout=10).json()

        print("\nJoke Time 🤣")
        print(json_data["setup"])
        input("Press Enter for punchline...")
        print(json_data["punchline"])

    # Loop

    again = input("\nDo you want to convert again? (y/n):").lower().strip()

    if again != "y":
        print("Goodbye!")
        break