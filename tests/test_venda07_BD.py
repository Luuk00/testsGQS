from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoBD import *
from queries_venda import *


class TestQueriesVenda(MockBD):

    def test_encontrar_vendas_mes_07(self):
        valor_esperado = [(3,), (4,), (6,), (8,), (10,)]
        self.assertEqual(ler_vendas_mes(self.mock_db_config.get('bd')), valor_esperado)

