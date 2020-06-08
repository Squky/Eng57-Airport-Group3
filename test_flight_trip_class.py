from unittest import TestCase
from passenger_subClass import *
from flight_trip_class import *
class TestFlight(TestCase):


    # Tests the "add_passenger" method of class Flight (flight_trip_class.py)
    # To test this method, a sample/test passenger must be created
    # and also a sample/test flight

    def test_add_passenger(self):
        test_passenger = Passenger("Bob",12345,"AJ8127393","Adult")
        test_flight = Flight("heath10550","JF1234","Portugal","United Kingdom",4,[])

        # The actuall assertion/test - this checks if the value returned from calling the method equals the expected
        # result
        self.assertTrue(test_flight.add_passenger(test_passenger)=="Bob added to the passenger list for flight JF1234")



    def test_get_details(self):
        test_flight = Flight("heath10550","JF1234", "Portugal", "United Kingdom", 4, [])
        test_output = {
            "Aircraft id   ": "heath10550",
            "Flight Number ": "JF1234",
            "Origin        ": "Portugal",
            "Destination   ": "United Kingdom",
            "Duraton       ": 4,
            "Passengers    ": []
        }
        self.assertTrue(test_flight.get_details() == test_output)







