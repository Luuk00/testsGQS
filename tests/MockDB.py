from unittest import TestCase

import sys
sys.path.insert(0, '..')
from conexaoBD import *

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()



        query_create_carro = """CREATE TABLE carro(
                                id int NOT NULL PRIMARY KEY,
                                nome text NOT NULL
                                )"""
        query_create_vendas = """CREATE TABLE vendas (
	                            id int NOT NULL PRIMARY KEY,
	                            mes text NOT NULL,
                                id_carro int NOT NULL,
                                FOREIGN KEY (id_carro) REFERENCES carro(id)
                                )"""
        try:
            cursor.execute(query_create_carro)
            cursor.execute(query_create_vendas)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_carro = """INSERT INTO carro (id, nome) VALUES
                                    (1, 'Gol'),
                                    (2, 'Uno'),
                                    (3, 'Palio'),
                                    (4, 'Ka'),
                                    (5, 'Chevette'),
                                    (6, 'Fusca')"""
        query_insert_vendas = """INSERT INTO vendas (id, mes, id_carro) VALUES
                                    (1, '6', 1),
                                    (2, '6', 2),
                                    (3, '7', 3),
                                    (4, '7', 1),
                                    (5, '6', 2),
                                    (6, '7', 3),
                                    (7, '6', 1),
                                    (8, '7', 2),
                                    (9, '6', 3),
                                    (10, '7', 1),
                                    (11, '11', 3),
                                    (12, '11', 1),
                                    (13, '12', 1),
                                    (14, '12', 2)
                                    """
        try:
            cursor.execute(query_insert_carro)
            cursor.execute(query_insert_vendas)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE carro")
            cursor.execute("DROP TABLE venda")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)



