from abc import ABC, abstractmethod

class AbstractPlant(ABC):

    def __init__(self, world=None):
       pass
        
    @abstractmethod
    def grow_up(self):
        pass
    
    @abstractmethod
    def get_illness_check(self):
        pass
    
    @abstractmethod
    def get_rid_of_illness_check(self):
        pass
    
    @abstractmethod
    def water(self):
        pass
    
    @abstractmethod
    def grow(self, plant, garden):
        pass