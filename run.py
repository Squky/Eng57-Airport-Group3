
## THIS CLASS IS FOR MANUAL TESTING AND UNDERSTANDING OF HOW CODE WORKS
## YOU CAN EDIT THIS AS YOU NEED


from flight_trip_class import *
from passenger_subClass import *

test_flight = Flight("heath10550","JF1234", "Portugal", "United Kingdom", 4, [])
test_passenger = Passenger("Bob",12345,"AJ8127393","Adult")

new_passenger = Passenger("Glad0s",10010, "TST475839","Advanced A.I")
test_flight.add_passenger(new_passenger)
test_flight.add_passenger(test_passenger)
test_flight.get_details()
# test_flight.get_details()

# print(test_flight.add_passenger(test_passenger))
# print("")
# test_flight.aircraft_id
#
# output = test_flight.get_details()
# test_output = {
#     "Aircraft id   ": "heath10550",
#     "Flight Number ": "JF1234",
#     "Origin        ": "Portugal",
#     "Destination   ": "United Kingdom",
#     "Duraton       ": 4,
#     "Passengers    ": ['Bob']
# }
# print(output==test_output)
#
# test_flight.update_aircraft("Spitfire")
