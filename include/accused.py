class accused():
    def __init__(self,first_name,last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__mi = None
        self.__dob = None
        self.__city = None
        self.__state = None
        self.__party = None
        
    def set_dob(self,new_dob):
        self.dob = new_dob
        
    def set_tar_data(self, mi=None, dob=None, city=None, state=None, party):
        self.__mi = mi
        self.__dob = dob
        self.__city = city
        self.__state = state
        self.__party = party