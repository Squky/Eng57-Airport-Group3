class Flight():

    def __init__(self,aircraft_id, flight_number, origin, destination, duration, passenger_list):
        self.aircraft_id = aircraft_id
        self.flight_num = flight_number
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.passenger_list = passenger_list

    def add_passenger(self, passenger):
        self.passenger_list.append(passenger.name)
        return f"{passenger.name} added to the passenger list for flight {self.flight_num}"

    def get_details(self):
        attributes = {
            "Aircraft id"   : self.aircraft_id,
            "Flight Number ": self.flight_num,
            "Origin        ": self.origin,
            "Destination   ": self.destination,
            "Duraton       ": self.duration,
            "Passengers    ": self.passenger_list
        }

        for key in attributes:
            print(key, " : ", attributes[key])

        return attributes

    def get_passengers(self):
        return self.passenger_list

    def update_aircraft(self,aircraft_id):
        user_input = input("Please enter your password: ")
        count = 5
        while count !=0:

            if(user_input == "SecretPassword123"):
                self.aircraft_id = aircraft_id
                break
            else:
                count-=1
                print(f"Sorry, incorrect password. You can try again {count} more times")

