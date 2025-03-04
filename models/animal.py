
from ianimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre:str, peso:float, edad:int)->None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def obtener_peso(self):
        return self._peso

    def obtener_edad(self):
        return self._edad