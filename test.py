from client import FlightSearchClient

client = FlightSearchClient()

#===== Flight Search =====#


# client.create__oneway_search_request(
#     dcity="DAC",
#     acity="DXB",
#     ddate="2025-12-15",
#     adult=1,
#     child=1,
#     # infant=1,
#     child_age=[9],
#     # infant_age=[1],
#     booking_class="Economy",
# )
# print("Search Result Completed xD")



#===== Flight Validation =====#



tracking_id = "71176484320417127YUTQ9"
flight_key = "F1EC00009-0"

# print(f"Checking validation for the flight key {tracking_id}")
# client.validate_flight(
#     data = [
#         {
#             "tracking_id": tracking_id,
#             "flight_key": flight_key
#         }
#     ]
# )
# print("Flight Validation Completed xD")


#===== Getting Validation Status =====#


booking_tracking_id = "71176484323917127WSD35"
# print("Getting Validation Status....", )
# client.get_validation_status(
#     booking_tracking_id=booking_tracking_id
# )
# print("Get Booking Validation Status Completed xD")

# ===== Updating Traveller Info =====#

# print("Updating Traveller Info....", )
# client.update_traveller_info(
#     booking_tracking_id=booking_tracking_id,
#     save_pax="yes",
#     passenger=[
#         {
#             "pax_id": "1",
#             "pax_type": "ADT", 
#             "gender": "M",
#             "title": "MR", 
#             "first_name": "Rakib",
#             "last_name": "Hasan",
#             "dob": "1991-10-24",
#             "nationality": "BD",
#             "doc_type": "passport", 
#             "doc_country": "BD",
#             "doc_no": "A1235121",
#             "doc_dateofexpiry": "2030-04-25",
#             "doc_dateofissue": "",
#             "frequent_flyer": "21321313132",
#             "isd_code": "880",
#             "contact_no": "1722222222",
#             "email_address": "xx@xxx.com",
#             "wheelchair_required": "no",
#             "special_request": "bla bla bla"
#         },
#         {
#             "pax_id": "2",
#             "pax_type": "CNN", 
#             "gender": "M",
#             "title": "Mstr", 
#             "first_name": "Child",
#             "last_name": "Test",
#             "dob": "2016-05-24",
#             "nationality": "BD",
#             "doc_type": "passport", 
#             "doc_country": "BD",
#             "doc_no": "A1235124",
#             "doc_dateofexpiry": "2030-04-25",
#             "doc_dateofissue": "",
#             "frequent_flyer": "21321313132",
#             "isd_code": "880",
#             "contact_no": "1722222222",
#             "email_address": "xx@xxx.com",
#             "wheelchair_required": "no",
#             "special_request": "bla bla bla"
#         }
#     ]
# )

# print("Update Traveller Info Completed xD")



#===== Create Booking =====#



# print("Creating Booking....", )
# client.create_booking(
#     booking_tracking_id=booking_tracking_id,
#     isd_code="880",
#     contact_no="1722222222",
#     email_address="demo@example.com",
#     payment_type="account_balance",
#     isPartialPay="no"
# )
# print("Create Booking Completed xD")



#===== Getting Booking Details =====#

booking_id = "FL2504DELHAASL"

# print("Getting Booking Details....", )
# client.get_booking_details(
#     tracking_id=booking_tracking_id,
#     booking_id=booking_id
# )

# print("Get Booking Details Completed xD")



#===== Issue Ticket =====#


print("Issuing Ticket....", )
client.issue_ticket(
    tracking_id=booking_tracking_id,
    price_change_accepted = "no",
    isPartialPay = "no",
    notes="not required",
    by_pass_partner_balance = "yes"
)
print("Issue Ticket Completed xD")







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