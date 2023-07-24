from historico import *

import unittest
class test_carro_historico(unittest.TestCase):
    def test_campeao_vendas_mensal(self):
        historico_mensal1 = {'Palio': 5, 'Uno': 7, 'Meriva': 3}
        historico_mensal2 = {'Palio': 0, 'Uno': 0, 'Meriva': 0}
        historico_mensal3 = {}

        lista_total_carros = ['Palio', 'Uno', 'Meriva', 'Compass']

        self.assertEqual(campeao_vendas_mensal(historico_mensal1, lista_total_carros), ('Uno', 0.5))
        self.assertEqual(campeao_vendas_mensal(historico_mensal2, lista_total_carros), ('Palio', 0.0))
        self.assertIsNone(campeao_vendas_mensal(historico_mensal3, lista_total_carros))