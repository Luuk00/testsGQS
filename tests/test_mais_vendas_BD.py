from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoBD import *
from queries_carros import *

class TestMaisVendas(MockBD):
    def test_encontrar_carros_mais_vendidos_mes_07(self):
        resultado_esperado = [('Palio')]
        self.assertEqual(carros_mais_vendas(self.mock_db_config.get('bd')), resultado_esperado)