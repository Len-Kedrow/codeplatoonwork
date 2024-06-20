
class CarManager:
    all_cars = []
    next_id = 1    
    total_cars = 0 

    def __init__(self, make, model, year, milage, services=None, id=None):
         
        self._make = make
        self._model = model
        self._year = year
        self._milage = milage
        self._service = services
        
        CarManager.next_id += 1 #increment next_id after asigning current id value
        CarManager.all_cars.append(self) #adds new instance to class attribute
        CarManager.total_cars = len(CarManager.all_cars) #calculates class attribute


    def __str__(self):
            return f"ID: {self._id}, MAKE: {self._make}, MODEL: {self._model}, YEAR: {self._year}, MILES: {self._milage}, SERVICE DUE: {self._service}"
       
        # def __repr__(self): 
        #      return (f"ID: {self._id} MAKE: {self._make} MODEL: {self._model} YEAR: {self._year} MILES: {self._milage} SERVICE DUE: {self._service}")
       
       
    @property
    def id(self):
            return self._id

    @id.setter  #Why do I needt this? Will I ever learn? 
    def set_id(self, new_id):
        if new_id > CarManager.next_id:
            self._id = new_id
        else:
            print(f" ")

    @id.deleter
    def delete_id(self):
        del self._id

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year
    @property
    def milage(self):
        return self._milage
    @property
    def service(self):
        return self._service


#----start replacemet code for above-----
    
    @classmethod
    def print_allcars(cls):
       for item in cls.all_cars:
             print(item)
    
#-----end code that replaces the above





    


        
