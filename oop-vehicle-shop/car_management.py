import rich

class CarManager:
    def __init__(self, make, model, year, milage, services=""):
        CarManager.all_cars = []
        CarManager.next_id = 1    
        CarManager.total_cars = 0 

        self._id = CarManager.next_id 
        self._make = make
        self._model = model
        self._year = year
        self._milage = milage
        self._service = services

        @property
        def id(self):
                return self._id

        @id.setter
        def price(self, new_id):
            if new_id > CarManager.next_id:
                self._id = new_id
            else:
                print(f" ")

        @id.deleter
        def price(self):
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
        
		
        


        
