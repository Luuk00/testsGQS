from estoque import *

import unittest

class TestCarroEstoque(unittest.TestCase):
    # [('Palio', 20), ('Uno', 10), ('Meriva', 4), ('Compass', 22)]
    def test_max_estoque(self):
        situacao1 = [('Palio', 20), ('Uno', 10), ('Meriva', 4), ('Compass', 22)]
        situacao2 = [('Palio', 20), ('Uno', 10), ('Meriva', 4), ('Compass', 20)]
        situacao3 = []

        self.assertEqual(max_estoque(situacao1), [('Compass', 22)])
        self.assertEqual(max_estoque(situacao2), [('Palio', 20), ('Compass', 20)])
        self.assertEqual(max_estoque(situacao3), [])