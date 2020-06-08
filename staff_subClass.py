from people_class import *

class Staff(People):

    def __init__(self,name,tax_num,staff_id,department):
        super().__init__(name,tax_num)
        self.__staff_id = staff_id
        self.__department = department
