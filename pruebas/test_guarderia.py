import unittest
from models.guarderia import Guarderia
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

class TestGuarderia(unittest.TestCase):
    def test_alimentar_boa(self):

        huron1 = Huron('Jhon', 5.3, 7, 'Colombia', 15.2)
        huron2 = Huron('Pedro', 3.0, 5, 'Peru', 11.4)

        boa1 = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 4)
        boa2 = Boa_Constrictor('Carlos', 10, 2, 'Chile', 11.2, 5)

        guarderia = Guarderia()

        guarderia.agregar_boa(boa1)
        guarderia.agregar_boa(boa2)

        self.assertIn(boa1, guarderia.obtener_boas())

        try:
            self.assertEqual(guarderia.obtener_boas()[0].alimentar_boa(),5)
            print(f'Boa alimentada')
        except ValueError as e:
            print(f'Boa llena {e}')

        try:
            self.assertEqual(guarderia.obtener_boas()[1].alimentar_boa(),6)
            print(f'Boa alimentada')
        except ValueError as e:
            print(f'Boa llena {e}')

    def test_alimentar_boa_llena(self):

        boa1 = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 10)
        boa2 = Boa_Constrictor('Carlos', 10, 2, 'Chile', 11.2, 5)

        guarderia = Guarderia()

        guarderia.agregar_boa(boa1)
        guarderia.agregar_boa(boa2)

        self.assertIn(boa1, guarderia.obtener_boas())

        try:
            self.assertEqual(guarderia.obtener_boas()[0].alimentar_boa(),8)
            print(f'Boa alimentada')
        except ValueError as e:
            print(f'Boa llena {e}')

    def test_alimentar_boa_no_existe(self):

        boa1 = Boa_Constrictor('Juan', 20, 5, 'Brasil', 20.1, 10)
        boa2 = Boa_Constrictor('Carlos', 10, 2, 'Chile', 11.2, 5)
        guarderia = Guarderia()

        guarderia.agregar_boa(boa1)
        guarderia.agregar_boa(boa2)
        self.assertIn(boa1, guarderia.obtener_boas())

        try:
            self.assertEqual(guarderia.obtener_boas()[2].alimentar_boa(),8)
            print(f'Boa alimentada')
        except IndexError:
            print(f'Boa no existe!')
        except ValueError as e:
            print(f'Boa llena {e}')

if __name__=='__main__':
    unittest.main()

