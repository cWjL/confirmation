class accused():
    def __init__(self,first_name,last_name,dob=None,city,state):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.city = city
        self.state = state
        
    def set_dob(self,new_dob):
        self.dob = new_dob