from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoBD import *
from queries_venda import *


class Testcarro(MockBD):
    def test_encontrar_carros_mes6(self):
        resultado_esperado = [(1,), (2,), (2,), (1,), (3,)]
        self.assertEqual(ler_vendas_mes6(self.mock_db_config.get('bd')), resultado_esperado)
    def test_encontrar_carros_mes7(self):
        resultado_esperado2 = [(3,), (1,), (3,), (2,), (1,)]
        self.assertEqual(ler_vendas_mes7(self.mock_db_config.get('bd')), resultado_esperado2)




 #   def test_ler_carro_mes(self):
 #       mes = '6'
 #       retorno_esperado_1 = []
        #retorno_esperado_2 = [('Palio,'), ('Gol',), ('Uno',)]
        # Obtém os carros vendidos nos meses 06 e 07
#        self.assertEqual(ler_carro_mes(self.mock_db_config.get('bd'), mes), retorno_esperado_1)
        #self.assertEqual(ler_carro_mes(self.mock_db_config.get('bd'), '7'), retorno_esperado_2)

