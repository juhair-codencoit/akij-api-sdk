import requests
import json
from pathlib import Path
from utils import write_response_to_file
import os
from dotenv import load_dotenv
load_dotenv()


class FlightSearchClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.secret_code = os.getenv("SECRET_KEY")
        self.base_url= os.getenv("BASE_URL")
        self.headers = {
            "apikey": self.api_key,
            "secretecode": self.secret_code
        }
    
    def search_flights(self, search_params):
        response = requests.post(f"{self.base_url}/flight/search", 
                                 json=search_params, 
                                 headers=self.headers)
        if response:
            write_response_to_file(
                response=response.json(),
                filename="search_response"
            )
        else:
            print("No data found")
            return None
        

body = {
    "journey_type": "OneWay", 
    "segment": [
        {
            "departure_airport_type": "AIRPORT", 
            "departure_airport": "DAC",
            "arrival_airport_type": "AIRPORT", 
            "arrival_airport": "DXB",
            "departure_date": "2025-11-15"
        }
    ],
    "travelers_adult": 1,
    "travelers_child": 1,
    "travelers_child_age": [
        9
    ],
    "travelers_infants": 1,
    "travelers_infants_age": [
        1
    ],
    "preferred_carrier": [],
    "non_stop_flight": "any", 
    "baggage_option": "any", 
    "booking_class": "Economy",
    "language": "en",
    "supplier_uid": "F1EC00009",
    "short_ref": "" 
}

client = FlightSearchClient()
client.search_flights(body)
print("Completed xD")