import requests
import json
from pathlib import Path
from typing import Dict, Optional, List
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
    
    def create__oneway_search_request(self,
                              dcity: str,
                              acity: str,
                              ddate: str,
                              adult: int = 1,
                              child: int = 0,
                              infant: int = 0,
                              child_age: Optional[List[int]] = None,
                              infant_age: Optional[List[int]] = None,
                              preferred_carrier: Optional[List[str]] = None,
                              non_stop_flight: Optional[str] = None,
                              baggage_option: Optional[str]= None,
                              booking_class: Optional[str]= None,
                              short_ref: Optional[str]= None
                              ):
        journey_type = "OneWay"
        dcity = dcity if dcity else None
        acity = acity if acity else None
        ddate = ddate if ddate else None
        adult = adult if adult else 1
        child = child if child else 0
        infant = infant if infant else 0
        child_age = child_age if child_age else []
        infant_age = infant_age if infant_age else []
        preferred_carrier = preferred_carrier if preferred_carrier else []
        non_stop_flight = non_stop_flight if non_stop_flight else "any"
        baggage_option = baggage_option if baggage_option else "any"
        booking_class = booking_class if booking_class else "Economy"
        language = "en"
        supplier_uid = "F1EC00009"
        short_ref = short_ref if short_ref else ""

        if child < 1:
            child_age = []
        if infant < 1:
            infant_age = []

        body = {
            "journey_type": journey_type, 
            "segment": [
                {
                    "departure_airport_type": "AIRPORT", 
                    "departure_airport": dcity,
                    "arrival_airport_type": "AIRPORT", 
                    "arrival_airport": acity,
                    "departure_date": ddate
                }
            ],
            "travelers_adult": adult,
            "travelers_child": child,
            "travelers_child_age": child_age,
            "travelers_infants": infant,
            "travelers_infants_age": infant_age,
            "preferred_carrier": preferred_carrier,
            "non_stop_flight": non_stop_flight, 
            "baggage_option": baggage_option, 
            "booking_class": booking_class,
            "language": language,
            "supplier_uid": supplier_uid,
            "short_ref": short_ref
        }


        response = requests.post(f"{self.base_url}/flight/search", 
                                 json=body, 
                                 headers=self.headers)
        if response:
            write_response_to_file(
                response=response.json(),
                filename="search_response"
            )
        else:
            print("No data found")
            return None
        


    def validate_flight(self,
                data: List[Dict],
        ):
        request_body = {
            "member_id": "1",
            "result_type": "general",
            "data": data
        }
        print(json.dumps(request_body, indent=4))
        try:
            response = requests.post(f"{self.base_url}/flight/validate", 
                                     json=request_body, 
                                     headers=self.headers)
            if response:
                write_response_to_file(
                    response=response.json(),
                    filename="validate_response"
                )
            else:
                print("No data found")
                return None
        except Exception as e:
            print(f"Error during flight validation: {e}")
            return None


