

class Airport:

    def __init__(self,terminal,flight_list):


        self.terminal = terminal
        self.flight_list = flight_list





    def add_flight(self, flight):
        self.flight_list.append(flight)
        return self.flight_list

    def get_flights(self):
        list=[]
        for i in self.flight_list:
            list.append(i.flight_num)
        return list

    def get_flight_details(self,flight_num):
        for i in self.flight_list:
            if (i.flight_num == flight_num):
                return i.get_details()

