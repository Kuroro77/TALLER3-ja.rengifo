

class Guarderia():
    def __init__(self)-> None:
        self.boas = []

    def agregar_boa(self, boa):
        self.boas.append(boa)

    def obtener_boas(self):
        return self.boas