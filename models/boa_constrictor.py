#from animal_exotico import Animal_Exotico
class Boa_Constrictor():
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float, ratones_comidos:int)->None:
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.pais_origen = pais_origen
        self.impuestos = impuestos
        self.__ratones_comidos = ratones_comidos

    def alimentar_boa(self):
        if self.__ratones_comidos == 10:
            raise ValueError("Demasiados ratones!")
        self.__ratones_comidos +=1
        return self.__ratones_comidos

    @property
    def dar_ratones_comidos(self):
        return self.__ratones_comidos

    def hacer_sonido(self)->str:
        return "¡Tsss!"

    def calcular_flete(self)->float:
        flete = self.impuestos * self.peso
        return flete