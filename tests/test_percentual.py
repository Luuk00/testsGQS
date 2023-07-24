from percentual import *

import unittest


class test_carro_percentural(unittest.TestCase):
    def test_aumento_queda_vendas(self):
        lista_percentuais = [('Meriva', 0.3, 0.4), ('Palio', 0.2, 0.22), ('Uno', 0.5, 0.1), ('Compass', 1, 0.4)]

        self.assertEqual(aumento_queda_vendas(lista_percentuais), [('Meriva', 0), ('Palio', 0), ('Uno', 1), ('Compass', 1)])
