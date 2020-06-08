from people_class import *

class Passenger(People):

    def __init__(self,name,tax_num,passport,pass_type):
        super().__init__(name,tax_num)
        self.passport = passport
        self.passenger_type = pass_type


    # def add_passenger(self,name,tax_num,passport,passType):
    #     super().__init__(name, tax_num)
    #     self.passport = passport
    #     self.passenger_type = passType



