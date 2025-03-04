import unittest
from models.boa_constrictor import Boa_Constrictor

class TestBoa_Constrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 2)
        self.assertEqual(boa.hacer_sonido(),"¡Tsss!")

    def test_calcular_flete(self):
        boa = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 2)
        self.assertEqual(boa.calcular_flete(),402.0)

    def test_agregar_raton(self):
        boa = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 5)
        self.assertEqual(boa.alimentar_boa(), 6)