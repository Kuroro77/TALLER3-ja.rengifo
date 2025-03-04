#from animal_exotico import Animal_Exotico

class Huron():
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"

    def calcular_flete(self)->float:
        flete = self.impuestos * self.peso
        return flete
