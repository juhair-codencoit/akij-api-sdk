from client import FlightSearchClient

client = FlightSearchClient()
# client.create__oneway_search_request(
#     dcity="DAC",
#     acity="DXB",
#     ddate="2025-12-15",
#     adult=1,
#     child=1,
#     infant=1,
#     child_age=[9],
#     infant_age=[1],
#     booking_class="Economy",
# )
# print("Search Result Completed xD")


tracking_id = "71176450126321032KFYFB"
flight_key = "F1EC00009-0"

print(f"Checking validation for the flight key {tracking_id}")
client.validate_flight(
    data = [
        {
            "tracking_id": tracking_id,
            "flight_key": flight_key
        }
    ]
)

print("Flight Validation Completed xD")








# body = {
#     "journey_type": "OneWay", 
#     "segment": [
#         {
#             "departure_airport_type": "AIRPORT", 
#             "departure_airport": "DAC",
#             "arrival_airport_type": "AIRPORT", 
#             "arrival_airport": "DXB",
#             "departure_date": "2025-11-15"
#         }
#     ],
#     "travelers_adult": 1,
#     "travelers_child": 1,
#     "travelers_child_age": [
#         9
#     ],
#     "travelers_infants": 1,
#     "travelers_infants_age": [
#         1
#     ],
#     "preferred_carrier": [],
#     "non_stop_flight": "any", 
#     "baggage_option": "any", 
#     "booking_class": "Economy",
#     "language": "en",
#     "supplier_uid": "F1EC00009",
#     "short_ref": "" 
# }