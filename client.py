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
    
    def create_search_request(self,
                              dcity,
                              acity,
                              ddate,
                              adult,
                              child,
                              infant,
                              child_age = [],
                              infant_age = [],
                              preferred_carrier=[],
                              non_stop_flight="any",
                              baggage_option="any",
                              booking_class="Economy",
                              language="en",
                              supplier_uid="F1EC00009",
                              short_ref=""
                              ):
        journey_type = "OneWay"
        dcity = dcity if dcity else None
        acity = acity if acity else None
        ddate = ddate if ddate else None
        adult = adult if adult else None
        child = child if child else None
        infant = infant if infant else None
        child_age = child_age if child_age else []
        infant_age = infant_age if infant_age else []
        preferred_carrier = preferred_carrier if preferred_carrier else []
        non_stop_flight = "any"
        baggage_option = "any"
        booking_class = "Economy"
        language = "en"
        supplier_uid = "F1EC00009"
        short_ref = ""

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