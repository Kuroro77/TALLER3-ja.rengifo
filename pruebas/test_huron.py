import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron('Jhon', 5.3, 7, 'Colombia', 15.2)
        self.assertEqual(huron.hacer_sonido(),"¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron('Jhon', 5.3, 7, 'Colombia', 15.2)
        self.assertEqual(huron.calcular_flete(),80.55999999999999)