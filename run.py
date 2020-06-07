
## THIS CLASS IS FOR MANUAL TESTING AND UNDERSTANDING OF HOW CODE WORKS
## YOU CAN EDIT THIS AS YOU NEED


from flight_trip_class import *
from passenger_subClass import *

test_flight = Flight("JF1234", "Portugal", "United Kingdom", 4, [])

test_flight.get_details()

test_output = {
    "Flight Number ": "JF1234",
    "Origin        ": "Portugal",
    "Destination   ": "United Kingdom",
    "Duraton       ": 4,
    "Passengers    ": []
}
