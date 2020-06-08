from people_class import *

class Staff(People):

    def __init__(self,name,tax_num,staff_id,department):
        super().__init__(name,tax_num)
        self.staff_id = staff_id
        self.department = department