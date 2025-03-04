from abc import ABC, abstractmethod

class iAnimal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass