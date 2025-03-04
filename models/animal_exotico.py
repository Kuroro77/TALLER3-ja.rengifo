from animal import Animal
class Animal_Exotico(Animal):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float)->None:
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self)->float:
        flete = self.__impuestos * self._peso
        return  flete