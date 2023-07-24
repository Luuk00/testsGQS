from conexaoBD import *

def ler_vendas_mes(bd):
    return ler_bd(bd, "SELECT id FROM vendas WHERE mes = 7")

def ler_vendas_mes6(bd):
    return ler_bd(bd, "SELECT id_carro FROM vendas WHERE mes = 6")
def ler_vendas_mes7(bd):
    return ler_bd(bd, "SELECT id_carro FROM vendas WHERE mes = 7")