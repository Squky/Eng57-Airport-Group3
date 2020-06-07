from people_class import *

class Passenger(People):

    def __init__(self,name,tax_num,passport):
        super().__init__(name,tax_num)
        self.passport = passport


