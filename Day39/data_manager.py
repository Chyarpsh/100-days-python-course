import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/83303377009cd7092e0b6167e5a64548/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.getenv("SHEETY_USRERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        pprint(data)
        if "prices" in data:
            self.destination_data = data["prices"]
        else:
            print("Key 'prices' not found in the data.")
            self.destination_data = []
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
