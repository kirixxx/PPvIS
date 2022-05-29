from abc import ABC, abstractmethod

class AbstractPest(ABC):
    def __init__(self):
        pass
    
    @abstractmethod    
    def attack_plant(self):
        pass